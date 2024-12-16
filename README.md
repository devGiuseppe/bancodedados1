# Projeto Banco de Dados 1  
**Autor:** Giuseppe Filippo Camardella Barbosa  
**RA:** 22121068-5  

---

## Como usar o código para gerar dados aleatórios  

1. Execute o código para gerar **5 arquivos CSV** contendo os dados necessários.  
2. Utilize as queries disponíveis no outro arquivo para importar os dados para o banco de dados.  
3. O código utiliza a biblioteca **Faker**:  
   - Para alterar a quantidade de dados gerados, modifique o `range` nos laços **for** ou ajuste as variáveis prefixadas com `num_`.

---

## Modelo Entidade-Relacionamento (MER)  

### Entidades e Atributos  

#### **Música**  
- `id_musica` (chave primária)  
- `titulo`  
- `duracao` (em segundos)  
- `id_disco` (chave estrangeira)  
  - Cada música pertence a um único disco.  

#### **Artista**  
- `id_artista` (chave primária)  
- `nome`  
- `data_nascimento`  
  - Um artista pode interpretar várias músicas e lançar vários discos.  

#### **Disco**  
- `id_disco` (chave primária)  
- `titulo`  
- `data_lancamento`  
- `id_artista` (chave estrangeira)  
  - Um disco pertence a um único artista e pode conter várias músicas.  

#### **Usuário**  
- `id_usuario` (chave primária)  
- `nome`  
- `email` (único)  
- `data_registro`  
  - Um usuário pode criar várias playlists.  

#### **Playlist**  
- `id_playlist` (chave primária)  
- `titulo`  
- `id_usuario` (chave estrangeira)  
  - Uma playlist é criada por um único usuário e pode conter várias músicas.  

#### **Música_Playlist** (Entidade Associativa)  
- `id_musica` (chave estrangeira)  
- `id_playlist` (chave estrangeira)  
  - Relaciona muitas músicas com muitas playlists.  

#### **Artista_Musica** (Entidade Associativa)  
- `id_artista` (chave estrangeira)  
- `id_musica` (chave estrangeira)  
  - Relaciona muitos artistas com muitas músicas.  

---

## Relacionamentos  

- **Disco → Música (1:N)**  
  Um disco contém várias músicas, mas uma música pertence a um único disco.  
  - **Chave estrangeira:** `id_disco` em Música.  

- **Artista → Disco (1:N)**  
  Um artista pode lançar vários discos, mas um disco pertence a um único artista.  
  - **Chave estrangeira:** `id_artista` em Disco.  

- **Artista → Música (N:N)**  
  Um artista pode interpretar várias músicas, e uma música pode ser interpretada por vários artistas.  
  - **Entidade associativa:** `Artista_Musica`.  

- **Usuário → Playlist (1:N)**  
  Um usuário pode criar várias playlists, mas cada playlist pertence a um único usuário.  
  - **Chave estrangeira:** `id_usuario` em Playlist.  

- **Playlist → Música (N:N)**  
  Uma playlist pode conter várias músicas, e uma música pode aparecer em várias playlists.  
  - **Entidade associativa:** `Música_Playlist`.  

---

## Modelo Relacional (3FN)  

As tabelas seguem a 3ª Forma Normal (3FN):  

### **Tabela Música**  
| Atributo     | Tipo       | Chave       |  
|--------------|------------|-------------|  
| id_musica    | PK         | Chave Primária |  
| titulo       | Texto      | -           |  
| duracao      | Inteiro    | -           |  
| id_disco     | FK         | Chave Estrangeira |  

### **Tabela Artista**  
| Atributo     | Tipo       | Chave       |  
|--------------|------------|-------------|  
| id_artista   | PK         | Chave Primária |  
| nome         | Texto      | -           |  
| data_nascimento | Data    | -           |  

### **Tabela Disco**  
| Atributo     | Tipo       | Chave       |  
|--------------|------------|-------------|  
| id_disco     | PK         | Chave Primária |  
| titulo       | Texto      | -           |  
| data_lancamento | Data    | -           |  
| id_artista   | FK         | Chave Estrangeira |  

### **Tabela Usuário**  
| Atributo     | Tipo       | Chave       |  
|--------------|------------|-------------|  
| id_usuario   | PK         | Chave Primária |  
| nome         | Texto      | -           |  
| email        | Texto Único| -           |  
| data_registro | Data      | -           |  

### **Tabela Playlist**  
| Atributo     | Tipo       | Chave       |  
|--------------|------------|-------------|  
| id_playlist  | PK         | Chave Primária |  
| titulo       | Texto      | -           |  
| id_usuario   | FK         | Chave Estrangeira |  

### **Tabela Música_Playlist**  
| Atributo     | Tipo       | Chave       |  
|--------------|------------|-------------|  
| id_musica    | FK         | Chave Estrangeira |  
| id_playlist  | FK         | Chave Estrangeira |  

### **Tabela Artista_Musica**  
| Atributo     | Tipo       | Chave       |  
|--------------|------------|-------------|  
| id_artista   | FK         | Chave Estrangeira |  
| id_musica    | FK         | Chave Estrangeira |  

---
## Diagrama  

Adicione uma imagem ou um link para visualizar o **Modelo Entidade-Relacionamento**:  

![Diagrama MER](https://github.com/user-attachments/assets/0e27a6f4-7b49-4ac3-a7c7-96c42c312de9)  
