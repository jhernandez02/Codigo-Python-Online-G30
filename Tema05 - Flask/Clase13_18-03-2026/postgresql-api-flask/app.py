# --*-- coding: utf-8 --*--
from flask import Flask, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname='api-flask',
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
    )
    conn.set_client_encoding('UTF8')
    return conn

def create_user_table():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(200) NOT NULL,
                email VARCHAR(200) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP        
            )
        ''')
        conn.commit()
        cur.close()
        conn.close()
        print('Table user created successfully')
    except Exception as e:
        print('Error creating table user:', e)

create_user_table()

def get_users_from_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

def insert_user_to_db(name: str, email: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO users (name, email) VALUES (%s, %s);',
        (name, email)
    )
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def home():
    return 'API REST con Flask 🐍'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    method = request.method

    try:
        if method == 'GET':
            users = get_users_from_db()

            users_list = []
            for user in users:
                users_list.append({
                    'id': user[0],
                    'name': user[1],
                    'email': user[2],
                    'created_at': str(user[3])
                })

            return users_list
        elif method == 'POST':
            json = request.get_json()
            name = json.get('name')
            email = json.get('email')
            insert_user_to_db(name, email)

            return {
                'message': 'User created successfully'
            }
    except Exception as e:
        return {
            'message': str(e)
        }
    
@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(user_id):
    method = request.method
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        if method == 'GET':
            cur.execute(
                'SELECT * FROM users WHERE id = %s;',
                (user_id,)
            )
            user = cur.fetchone()

            if not user:
                raise Exception('User not found')
            
            return {
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'created_at': str(user[3])
            }
        elif method == 'PUT':
            json = request.get_json()
            name = json.get('name')
            email = json.get('email')

            cur.execute(
                'UPDATE users SET name = %s, email = %s WHERE id = %s;',
                (name, email, user_id)
            )
            conn.commit()

            if cur.rowcount == 0:
                raise Exception('User not found')
            
            return {
                'message': 'User updated successfully'
            }
        elif method == 'DELETE':
            cur.execute(
                'DELETE FROM users WHERE id = %s;',
                (user_id,)
            )
            conn.commit()

            if cur.rowcount == 0:
                raise Exception('User not found')
        
            return {
                'message': 'User deleted successfully'
            }
    except Exception as e:
        return {
            'message': str(e)
        }
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)