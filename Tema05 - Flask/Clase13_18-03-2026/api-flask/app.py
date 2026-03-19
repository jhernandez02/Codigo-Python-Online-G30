from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola, bienvenido a mi API Flask! 🐍'

@app.route('/user', methods=["GET", "POST", "PUT", "DELETE"])
def users():
    method = request.method

    if method == "GET":
        return {
            'id': 1,
            'name': 'Jhon Doe',
            'email': 'jhon@example.com',
        }
    elif method == "POST":
        json = request.get_json()
        return json

@app.route('/users/<name>') # <int:user_id>, <string:name>, <float:price>, <path:path>, <uuid:uuid>
def user(name):
    return f'Hola {name}'

@app.route('/users/<int:user_id>', methods=["PUT"])
def update_user(user_id):
    json = request.get_json()
    name = json.get('name')
    email = json.get('email')
    return {
        'id': user_id,
        'name': name,
        'email': email
    }

if __name__ == '__main__':
    app.run(debug=True)