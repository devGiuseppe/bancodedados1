import csv
from faker import Faker
import random

fake = Faker()

# Função para gerar Artistas
def gerar_artistas(n):
    artistas = []
    for _ in range(n):
        artista = {
            'nome': fake.name(),
            'data_nascimento': fake.date_of_birth(minimum_age=18, maximum_age=70)
        }
        artistas.append(artista)
    return artistas

# Função para gerar Discos
def gerar_discos(n, artistas):
    discos = []
    for _ in range(n):
        disco = {
            'titulo': fake.sentence(nb_words=3),
            'data_lancamento': fake.date_this_decade(),
            'artista': random.choice(artistas)['nome']  # Relacionar disco a um artista
        }
        discos.append(disco)
    return discos

# Função para gerar Músicas
def gerar_musicas(n, discos, artistas):
    musicas = []
    for _ in range(n):
        musica = {
            'titulo': fake.sentence(nb_words=2),
            'duracao': random.randint(120, 360),  # Duração entre 2 e 6 minutos (em segundos)
            'disco': random.choice(discos)['titulo'],
            'artistas': [random.choice(artistas)['nome'] for _ in range(random.randint(1, 3))]  # Até 3 artistas
        }
        musicas.append(musica)
    return musicas

# Função para gerar Playlists
def gerar_playlists(n, usuarios, musicas):
    playlists = []
    for _ in range(n):
        playlist = {
            'titulo': fake.sentence(nb_words=3),
            'usuario': random.choice(usuarios)['nome'],
            'musicas': [random.choice(musicas)['titulo'] for _ in range(random.randint(5, 15))]  # Playlist com 5 a 15 músicas
        }
        playlists.append(playlist)
    return playlists

# Função para gerar Usuários
def gerar_usuarios(n):
    usuarios = []
    for _ in range(n):
        usuario = {
            'nome': fake.name(),
            'email': fake.unique.email(),
            'data_registro': fake.date_this_year()
        }
        usuarios.append(usuario)
    return usuarios

# Função para salvar dados em CSV
def salvar_csv(dados, colunas, arquivo):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(colunas)  # Cabeçalho
        for dado in dados:
            writer.writerow([dado[coluna] for coluna in colunas])

# Gerar os dados
num_registros = 200
num_musicas = 1000  # Ajuste para 1000 músicas
usuarios = gerar_usuarios(num_registros)
artistas = gerar_artistas(num_registros)
discos = gerar_discos(num_registros, artistas)
musicas = gerar_musicas(num_musicas, discos, artistas)
playlists = gerar_playlists(num_registros, usuarios, musicas)

# Salvar cada entidade em CSV
salvar_csv(usuarios, ['nome', 'email', 'data_registro'], 'usuarios.csv')
salvar_csv(artistas, ['nome', 'data_nascimento'], 'artistas.csv')
salvar_csv(discos, ['titulo', 'data_lancamento', 'artista'], 'discos.csv')
salvar_csv(musicas, ['titulo', 'duracao', 'disco', 'artistas'], 'musicas.csv')
salvar_csv(playlists, ['titulo', 'usuario', 'musicas'], 'playlists.csv')
