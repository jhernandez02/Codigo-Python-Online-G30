from app.models.user_model import User
from app.schemas.user_schema import UserSchema
from db import db

class UserService:
    def get_all(self):
        users = User.query.all()
        return users
    
    def create(self, data: UserSchema):
        user = User(
            name=data.name,
            email=data.email,
            password=data.password,
            role_id=data.role_id
        )
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, data):
        pass

    def delete(self, data):
        pass
    
    def get_by_id(self, id):
        pass

user_service = UserService()