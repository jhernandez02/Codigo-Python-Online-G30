from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
import bcrypt
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token
from datetime import timedelta

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-auth'
app.config['JWT_SECRET_KEY'] = 'secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(weeks=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(Text)

with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST', 'GET'])
def users():
    method = request.method
    try:
        if method == 'POST':
            data = request.get_json()

            user = User.query.filter_by(
                email=data.get('email')
            ).first()

            if user:
                raise Exception('User already exists')
            

            bytes_password = data.get('password').encode('utf-8')
            hashed_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
            string_hashed_password = hashed_password.decode('utf-8')
            
            created_user = User(
                name=data.get('name'),
                email=data.get('email'),
                password=string_hashed_password
            )

            db.session.add(created_user)
            db.session.commit()

            return {
                'id': created_user.id,
                'name': created_user.name,
                'email': created_user.email
            }
    except Exception as e:
        return {
            'message': str(e)
        }, 400

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        user = User.query.filter_by(
            email=data.get('email')
        ).first()

        if not user:
            raise Exception('Invalid credentials')
        
        bytes_user_password = user.password.encode('utf-8')
        bytes_data_password = data.get('password').encode('utf-8')
        is_correct_password = bcrypt.checkpw(bytes_data_password, bytes_user_password)

        if not is_correct_password:
            raise Exception('Invalid credentials')

        access_token = create_access_token(
            identity=user.id
        )
        refresh_token = create_refresh_token(
            identity=user.id
        )

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    except Exception as e:
        return {
            'message': str(e)
        }, 400

if __name__ == '__main__':
    app.run(debug=True)