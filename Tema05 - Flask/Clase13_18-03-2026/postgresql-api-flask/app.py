from flask import Flask
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

@app.route('/')
def home():
    return 'API REST con Flask 🐍'

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()

    users_list = []
    for user in users:
        users_list.append({
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'created_at': str(user[3])
        })

    return users_list

if __name__ == '__main__':
    app.run(debug=True)