from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola, bienvenido a mi API Flask! 🐍'

@app.route('/users', methods=["GET", "POST", "PUT", "DELETE"])
def users():
    return 'Usuarios'


if __name__ == '__main__':
    app.run(debug=True)