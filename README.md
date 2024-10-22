# bancodedados1
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
