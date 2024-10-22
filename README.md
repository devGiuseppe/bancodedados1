# Projeto bancodedados1 Giuseppe Filippo Camardella Barbosa RA: 22121068-5
Como usar o código para gerar dados aleatórios:
run gera 5 arquivos csv que usando as queries do outro arquivo você consegue mandar para o banco de dados
o código foi feito pela biblioteca faker e para alterar as quantidades é só mudar o range dos for ou das variáveis num_.

Modelo Entidade-Relacionamento
Entidades e Atributos:

Música

Atributos:
id_musica (chave primária)
titulo
duracao (em segundos)
id_disco (chave estrangeira)
Cada música pertence a um único disco.
Artista

Atributos:
id_artista (chave primária)
nome
data_nascimento
Um artista pode interpretar várias músicas e lançar vários discos.
Disco

Atributos:
id_disco (chave primária)
titulo
data_lancamento
id_artista (chave estrangeira)
Um disco pertence a um único artista e pode conter várias músicas.
Usuário

Atributos:
id_usuario (chave primária)
nome
email (único)
data_registro
Um usuário pode criar várias playlists.
Playlist

Atributos:
id_playlist (chave primária)
titulo
id_usuario (chave estrangeira)
Uma playlist é criada por um único usuário e pode conter várias músicas.
Música_Playlist (Entidade associativa para representar o relacionamento entre músicas e playlists)

Atributos:
id_musica (chave estrangeira)
id_playlist (chave estrangeira)
Esta entidade relaciona muitas músicas com muitas playlists.
Artista_Musica (Entidade associativa para representar o relacionamento entre artistas e músicas)

Atributos:
id_artista (chave estrangeira)
id_musica (chave estrangeira)
Esta entidade relaciona muitos artistas com muitas músicas.


Relacionamentos:

Disco → Música (1
)

Um disco contém várias músicas, mas uma música pertence a um único disco.
Chave estrangeira: id_disco em Música.
Artista → Disco (1
)

Um artista pode lançar vários discos, mas um disco pertence a um único artista.
Chave estrangeira: id_artista em Disco.
Artista → Música (N
)

Um artista pode interpretar várias músicas, e uma música pode ser interpretada por vários artistas.
Entidade associativa: Artista_Musica com chaves estrangeiras id_artista e id_musica.
Usuário → Playlist (1
)

Um usuário pode criar várias playlists, mas cada playlist pertence a um único usuário.
Chave estrangeira: id_usuario em Playlist.
Playlist → Música (N
)

Uma playlist pode conter várias músicas, e uma música pode aparecer em várias playlists.
Entidade associativa: Música_Playlist com chaves estrangeiras id_playlist e id_musica.

Modelo Entidade-Relacionamento (MER):
![mre drawio](https://github.com/user-attachments/assets/0e27a6f4-7b49-4ac3-a7c7-96c42c312de9)

Entidades:

Música (id_musica, titulo, duracao, id_disco)

Artista (id_artista, nome, data_nascimento)

Disco (id_disco, titulo, data_lancamento, id_artista)

Usuário (id_usuario, nome, email, data_registro)

Playlist (id_playlist, titulo, id_usuario)

Artista_Musica (id_artista, id_musica)

Música_Playlist (id_playlist, id_musica)


Relacionamentos:

Disco contém várias músicas (1
entre Disco e Música).

Um artista interpreta várias músicas (N
entre Artista e Música).

Um usuário cria várias playlists (1
entre Usuário e Playlist).

Uma playlist pode conter várias músicas (N
entre Playlist e Música).

Diagramas e Cardinalidade:

Disco ↔ Música (1
)

Artista ↔ Disco (1
)

Artista ↔ Música (N
via Artista_Musica)

Usuário ↔ Playlist (1
)

Playlist ↔ Música (N
via Música_Playlist)


Tabelas Relacionais na 3FN:

1. Tabela Musica

Atributos:

id_musica (PK)
titulo
duracao
id_disco (FK)
Descrição:

  Cada música tem um título e duração, e está associada a um disco (chave estrangeira id_disco).

3. Tabela Artista

Atributos:

id_artista (PK)
nome
data_nascimento
Descrição:

  Armazena os dados de cada artista.
  
5. Tabela Disco

Atributos:

id_disco (PK)
titulo
data_lancamento
id_artista (FK)
Descrição: 
Cada disco tem um título e data de lançamento, e está associado a um único artista (chave estrangeira id_artista).

7. Tabela Usuario

Atributos:

id_usuario (PK)
nome
email (único)
data_registro
Descrição:
Armazena informações dos usuários, com um email único para cada usuário.

9. Tabela Playlist

Atributos:

id_playlist (PK)
titulo
id_usuario (FK)
Descrição:
Cada playlist pertence a um único usuário, identificada por id_usuario.

11. Tabela Musica_Playlist (Entidade associativa para o relacionamento N
entre Musica e Playlist)

Atributos:

id_musica (FK)
id_playlist (FK)
Descrição:
  Tabela de relacionamento entre músicas e playlists. Uma música pode aparecer em várias playlists e uma playlist pode conter várias músicas.
13. Tabela Artista_Musica (Entidade associativa para o relacionamento N
entre Artista e Musica)

Atributos:

id_artista (FK)
id_musica (FK)
Descrição:
 Tabela de relacionamento entre artistas e músicas. Um artista pode interpretar várias músicas, e uma música pode ser interpretada por vários artistas.
 ![image](https://github.com/user-attachments/assets/2e1bc17b-d04e-4dcc-acd9-a135060acf1f)
 
 (é uma imagem gerada mas eu achei que ficou bonito)
