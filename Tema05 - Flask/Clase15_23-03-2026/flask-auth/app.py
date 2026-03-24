from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
import bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(Text)

with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def users():
    method = request.method
    if method == 'POST':
        data = request.get_json()

        user = User.query.filter_by(
            email=data.get('email')
        ).first()

        if user:
            raise Exception('User already exists')
        
        User(
            name=data.get('name'),
            email=data.get('email'),
            password=''
        )

if __name__ == '__main__':
    app.run(debug=True)