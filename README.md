
# Projeto Banco de Dados 1  
**Autor:** Giuseppe Filippo Camardella Barbosa  
**RA:** 22121068-5  

---

## Como usar o código para gerar dados aleatórios  

1. Execute o código para gerar **5 arquivos CSV** contendo os dados necessários.  
2. Utilize as queries disponíveis no outro arquivo para importar os dados para o banco de dados.**atualizado no arquivo python tem as queries também.  
3. O código utiliza a biblioteca **Faker**:  
   - Para alterar a quantidade de dados gerados, modifique o `range` nos laços **for** ou ajuste as variáveis prefixadas com `num_`.

---

## Como conectar ao PostgreSQL e executar o código  

### 1. **Instalar o PostgreSQL**
Baixe e instale o PostgreSQL.

Após a instalação, verifique se o PostgreSQL está funcionando corretamente com:
```bash
psql --version
```

### 2. **Criar um Banco de Dados no PostgreSQL**
Após a instalação do PostgreSQL:

- Abra o terminal e entre no PostgreSQL:
  ```bash
  psql -U postgres
  ```
  Isso solicitará a senha do usuário `postgres` (se configurada).
  
- Crie um banco de dados:
  ```sql
  CREATE DATABASE seu_banco_de_dados;
  ```

### 3. **Instalar as Dependências**
Instale o `psycopg2` para conectar o Python ao PostgreSQL:
```bash
pip install psycopg2
```
Ou a versão binária mais leve:
```bash
pip install psycopg2-binary
```

### 4. **Configuração do Código**
No código Python, dentro da função `conectar_postgres()`, configure as credenciais de conexão com o PostgreSQL:

```python
def conectar_postgres():
    return psycopg2.connect(
        dbname="cascalitos",   # Nome do banco de dados, pode colocar oque quiser
        user="teste_usuario",             # Usuário
        password="teste_senha",           # Senha do usuário
        host="localhost",               
        port="5432"                     # Porta padrão do PostgreSQL, pode mudar se quiser
    )
```

- **dbname**: O nome do banco de dados que você criou.
- **user**: Usuário do PostgreSQL (geralmente 'postgres').
- **password**: Senha configurada para o usuário.
- **host**: Normalmente `localhost` para banco de dados local.
- **port**: A porta padrão é `5432`.

### 5. **Executar o Código**
Para rodar o código Python, no terminal ou em uma IDE, execute:

```bash
python gerardados.py
```

Isso vai fazer:
1. Conectar ao banco de dados PostgreSQL.
2. Criar as tabelas necessárias.
3. Gerar e inserir dados sintéticos nas tabelas.

### 6. **Verificar os Dados no PostgreSQL**
Para visualizar os dados inseridos, use o `psql`:

1. Abra o terminal e entre no PostgreSQL:
   ```bash
   psql -U postgres
   ```

2. Conecte-se ao banco de dados criado:
   ```sql
   \c seu_banco_de_dados
   ```

3. Consulte os dados nas tabelas:
   ```sql
   SELECT * FROM usuarios;
   SELECT * FROM artistas;
   SELECT * FROM discos;
   ```

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

![Diagrama MER](https://github.com/user-attachments/assets/0e27a6f4-7b49-4ac3-a7c7-96c42c312de9)  
