from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-sqlalchemy'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())

    def __str__(self):
        return self.name

with app.app_context():
    db.create_all()

@app.route("/users", methods=['GET', 'POST'])
def users():
    method = request.method
    try:
        if method == 'GET':
            users = User.query.all() # SELECT * FROM users
            
            users_list = []
            for user in users:
                users_list.append({
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'created_at': str(user.created_at)
                })

            return users_list
        elif method == 'POST':
            data = request.get_json()
            user = User(
                name=data.get('name'),
                email=data.get('email'),
                password=data.get('password')
            )
            db.session.add(user)
            db.session.commit()
            return {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'created_at': str(user.created_at)
            }
    except Exception as e:
        return {
            'message': str(e)
        }, 400

@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def user(user_id: int):
    method = request.method
    try:
        if method == 'GET':
            user = User.query.get(user_id)
            # user = User.query.filter_by(id=user_id).first()
            if not user:
                raise Exception('User not found')

            return {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'created_at': str(user.created_at)
            }
        if method == 'PUT':
            data = request.get_json()
            user = User.query.get(user_id)

            if not user:
                raise Exception('User not found')

            user.name = data.get('name')
            user.email = data.get('email')
            user.password = data.get('password')

            db.session.commit()
            return {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'created_at': str(user.created_at)
            }
        if method == 'DELETE':
            user = User.query.get(user_id)
            
            if not user:
                raise Exception('User not found')
            
            db.session.delete(user)
            db.session.commit()

            return {
                'message': 'Used deleted'
            }
    except Exception as e:
        return {
            'message': str(e)
        }, 400

@app.route("/")
def home():
    return "Hello World! 🐍"

if __name__ == "__main__":
    app.run(debug=True)