import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user='postgres',
    password='0112'
    # user=os.environ['DB_USER_PSQL'],
    # password=os.environ['DB_PASSWORD_PSQL']
)

cur = conn.cursor()

cur.execute('Drop table if exist clientes;')
cur.execute('CREATE TABLE clientes(id SERIAL PRIMARY KEY,'
                                'nome varchar(100) NOT NULL,'
                                'sobrenome varchar(100) NOT NULL);'
)

cur.execute(
    'INSERT INTO clientes(nome, sobrenome) VALUES (%s,%s)',
    ('Tom','Farias')
)

conn.commit()

cur.close()
conn.close()