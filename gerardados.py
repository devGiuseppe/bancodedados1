import csv
import random
import psycopg2
from faker import Faker

fake = Faker()

# Função para conectar ao PostgreSQL
def conectar_postgres():
    return psycopg2.connect(
        dbname="cascalitos",#aqui colocar o nome do banco que quer usar
        user="usuario_teste",#aqui colocar o nome seu usuário
        password="senha_teste",#aqui colocar a sua senha
        host="localhost",
        port="5432"#aqui a porta que quer ultilizar
    )

# Função para criar tabelas no banco de dados ou pode ultilizar as queries manualmente 
def criar_tabelas(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            data_registro DATE
        );

        CREATE TABLE IF NOT EXISTS artistas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255),
            data_nascimento DATE
        );

        CREATE TABLE IF NOT EXISTS discos (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(255),
            data_lancamento DATE,
            artista_id INT REFERENCES artistas(id)
        );

        CREATE TABLE IF NOT EXISTS musicas (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(255),
            duracao INT,
            disco_id INT REFERENCES discos(id)
        );

        CREATE TABLE IF NOT EXISTS playlists (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(255),
            usuario_id INT REFERENCES usuarios(id)
        );

        CREATE TABLE IF NOT EXISTS playlist_musicas (
            playlist_id INT REFERENCES playlists(id),
            musica_id INT REFERENCES musicas(id),
            PRIMARY KEY (playlist_id, musica_id)
        );
        """)
        conexao.commit()

# Funções para inserir dados

def inserir_usuarios(conexao, usuarios):
    with conexao.cursor() as cursor:
        for usuario in usuarios:
            cursor.execute(
                "INSERT INTO usuarios (nome, email, data_registro) VALUES (%s, %s, %s)",
                (usuario['nome'], usuario['email'], usuario['data_registro'])
            )
        conexao.commit()

def inserir_artistas(conexao, artistas):
    with conexao.cursor() as cursor:
        for artista in artistas:
            cursor.execute(
                "INSERT INTO artistas (nome, data_nascimento) VALUES (%s, %s)",
                (artista['nome'], artista['data_nascimento'])
            )
        conexao.commit()

def inserir_discos(conexao, discos, artistas):
    with conexao.cursor() as cursor:
        for disco in discos:
            cursor.execute(
                "SELECT id FROM artistas WHERE nome = %s",
                (disco['artista'],)
            )
            artista_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO discos (titulo, data_lancamento, artista_id) VALUES (%s, %s, %s)",
                (disco['titulo'], disco['data_lancamento'], artista_id)
            )
        conexao.commit()

def inserir_musicas(conexao, musicas, discos):
    with conexao.cursor() as cursor:
        for musica in musicas:
            cursor.execute(
                "SELECT id FROM discos WHERE titulo = %s",
                (musica['disco'],)
            )
            disco_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO musicas (titulo, duracao, disco_id) VALUES (%s, %s, %s)",
                (musica['titulo'], musica['duracao'], disco_id)
            )
        conexao.commit()

def inserir_playlists(conexao, playlists, usuarios, musicas):
    with conexao.cursor() as cursor:
        for playlist in playlists:
            cursor.execute(
                "SELECT id FROM usuarios WHERE nome = %s",
                (playlist['usuario'],)
            )
            usuario_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO playlists (titulo, usuario_id) VALUES (%s, %s) RETURNING id",
                (playlist['titulo'], usuario_id)
            )
            playlist_id = cursor.fetchone()[0]

            for musica_titulo in playlist['musicas']:
                cursor.execute(
                    "SELECT id FROM musicas WHERE titulo = %s",
                    (musica_titulo,)
                )
                musica_id = cursor.fetchone()[0]
                cursor.execute(
                    "INSERT INTO playlist_musicas (playlist_id, musica_id) VALUES (%s, %s)",
                    (playlist_id, musica_id)
                )
        conexao.commit()

# Funções para gerar dados

def gerar_usuarios(n):
    return [{
        'nome': fake.name(),
        'email': fake.unique.email(),
        'data_registro': fake.date_this_year()
    } for _ in range(n)]

def gerar_artistas(n):
    return [{
        'nome': fake.name(),
        'data_nascimento': fake.date_of_birth(minimum_age=18, maximum_age=70)
    } for _ in range(n)]

def gerar_discos(n, artistas):
    return [{
        'titulo': fake.sentence(nb_words=3),
        'data_lancamento': fake.date_this_decade(),
        'artista': random.choice(artistas)['nome']
    } for _ in range(n)]

def gerar_musicas(n, discos):
    return [{
        'titulo': fake.sentence(nb_words=2),
        'duracao': random.randint(120, 360),
        'disco': random.choice(discos)['titulo']
    } for _ in range(n)]

def gerar_playlists(n, usuarios, musicas):
    return [{
        'titulo': fake.sentence(nb_words=3),
        'usuario': random.choice(usuarios)['nome'],
        'musicas': [random.choice(musicas)['titulo'] for _ in range(random.randint(5, 15))]
    } for _ in range(n)]

# Script principal
if __name__ == "__main__":
    conexao = conectar_postgres()
    criar_tabelas(conexao)

    num_registros = 200
    num_musicas = 1000

    usuarios = gerar_usuarios(num_registros)
    artistas = gerar_artistas(num_registros)
    discos = gerar_discos(num_registros, artistas)
    musicas = gerar_musicas(num_musicas, discos)
    playlists = gerar_playlists(num_registros, usuarios, musicas)

    inserir_usuarios(conexao, usuarios)
    inserir_artistas(conexao, artistas)
    inserir_discos(conexao, discos, artistas)
    inserir_musicas(conexao, musicas, discos)
    inserir_playlists(conexao, playlists, usuarios, musicas)

    conexao.close()
