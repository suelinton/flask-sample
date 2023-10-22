1- DOWNLOAD PYTHON 3.12
2- DOWNLOAD VSCODE E PYTHON FOR VSCODE EXTENSION
3- configura permisões de politicas do prontp
  >Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
4- CONFIGURA .VENV
    > mkdir myproject
    > cd myproject
    > py -3 -m venv .venv
    > .venv\Scripts\activate
5- instala o flask 2.0.2
    > pip install Flask==2.0.2
6- cria o arquivo inicial app.py
7- Download postgresSql
    [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads]
8- Configurar postgrese
    -[https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application]
    >CREATE DATABASE flask_db;
    >CREATE USER sammy WITH PASSWORD 'password';
    >GRANT ALL PRIVILEGES ON DATABASE flask_db TO sammy;
    >\l
    >\q
9- Configurar "Microsoft C++ Build Tools"
    - faz o dowload em do C++ Build Tools https://visualstudio.microsoft.com/visual-cpp-build-tools/
    - configura individualmente apenas o que precisar

10 -Configurar driver postgres para python
    >pip install psycopg2-binary
11- configura init_db.py
12- configura variavel de ambiente de usuario
    >set DB_USERNAME=""
    >SET DB_PASSWORD=""
13- roda o init_db
    >python init_db.py
14 - cria o app.py
15 - roda o flask 
  > flask --app app run