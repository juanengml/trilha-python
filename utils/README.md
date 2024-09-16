# Documentação: Como Usar o Replit e Configurar Flask e MySQL

Este guia irá te orientar a usar o Replit para desenvolvimento, além de configurar Flask e MySQL para seus projetos.

---

## 1. Criando um Projeto no Replit
1. Acesse o [Replit](https://replit.com/).
2. Clique no botão **+ Create Repl**.
3. Selecione a linguagem **Python**.
4. Dê um nome ao seu projeto e clique em **Create Repl**.
5. O ambiente de desenvolvimento será iniciado, e você verá uma interface de código, terminal e outras ferramentas úteis.

---

## 2. Instalando Flask no Replit
1. No painel esquerdo, clique na aba **Packages**.
2. No campo de busca, procure por .
3. Clique no botão **+** para instalar o Flask no seu projeto.
4. Agora você pode adicionar o seguinte código no arquivo  para iniciar uma aplicação Flask:
5. Após isso, clique no botão **Run** no topo da tela para executar sua aplicação Flask.

---

Aqui está a versão ajustada do tutorial usando o serviço gratuito de banco de dados MySQL [FreeDB.tech](https://freedb.tech):

---

## 3. Instalando e Configurando MySQL no Replit

### Utilizando um Banco de Dados Externo MySQL com FreeDB.tech

O Replit não suporta nativamente um banco de dados MySQL local, mas você pode usar o [FreeDB.tech](https://freedb.tech), um serviço gratuito de banco de dados MySQL.

### Passos Simples para Configurar um Banco de Dados MySQL no FreeDB.tech:

1. **Crie uma conta no FreeDB.tech**:
   - Acesse [FreeDB.tech](https://freedb.tech).
   - Registre-se e crie um banco de dados MySQL.

2. **No Replit, instale o pacote `mysql-connector-python`**:
   - No painel esquerdo do Replit, clique na aba **Packages**.
   - No campo de busca, digite `mysql-connector-python`.
   - Clique em **+** para instalar o pacote.

3. **Conectando ao Banco de Dados**:
   Use o código abaixo para se conectar ao banco de dados MySQL que você criou no FreeDB.tech:

   ```python
   import mysql.connector

   # Substitua pelos detalhes do seu banco no FreeDB.tech
   db = mysql.connector.connect(
       host="freedb.tech",       # Host do banco
       user="seu-usuario",       # Usuário do FreeDB.tech
       password="sua-senha",     # Senha do FreeDB.tech
       database="seu-banco"      # Nome do banco de dados
   )

   cursor = db.cursor()

   # Testa a conexão listando as tabelas do banco de dados
   cursor.execute("SHOW TABLES")

   for table in cursor:
       print(table)
   ```

4. **Teste a Conexão**:
   - Execute o código no Replit.
   - Se a conexão estiver configurada corretamente, você verá a lista de tabelas do banco de dados (ou nada, se o banco estiver vazio).

---

## 4. Executando o Projeto no Replit
- Clique no botão **Run** no topo da tela.
- O servidor Flask será executado, e você verá um link no lado direito, no painel de execução, onde poderá acessar sua aplicação.
- Certifique-se de que a sua aplicação Flask está rodando corretamente e conectada ao banco de dados MySQL.

---

## 5. Entregáveis no Replit
- Ao concluir cada exercício ou projeto, envie o link de compartilhamento do seu Replit.
- Para gerar o link, clique no botão **Share** no canto superior direito da tela do Replit.
- Certifique-se de que sua aplicação está funcional e a demonstração está disponível via link.

---

## 6. Dicas Úteis para o Replit
- **Ambiente colaborativo**: O Replit permite que você convide outros usuários para colaborar no seu código em tempo real.
- **Logs e erros**: Utilize o painel de execução à direita para visualizar logs e erros que ocorrem durante a execução do seu código.
- **Instalação de pacotes**: Todos os pacotes necessários podem ser instalados diretamente na aba **Packages**.

