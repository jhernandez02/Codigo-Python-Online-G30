from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
import bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-auth'

db = SQLAlchemy()

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

if __name__ == '__main__':
    app.run(debug=True)