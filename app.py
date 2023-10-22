from flask import Flask, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database='flask_db',
        user= 'postgres',
        password='0112'
    )
    return conn

@app.route('/clientes',methods=['POST','GET'])
def clientes():
    if request.method == 'POST':
        print('fluxo de post')
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('INSERT INTO clientes(nome, sobrenome) values (%s, %s)', (nome, sobrenome))
        conn.commit()
        cur.close()
        conn.close()
        return 'Inserido com sucesso'
    else:
        print('fluxo de get')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('select * from clientes;')
        clientes = cur.fetchall()
        cur.close()
        conn.close()

    return clientes


