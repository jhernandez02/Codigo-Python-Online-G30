from app.models.user_model import User
from app.schemas.user_schema import CreateUserSchema
from db import db

class UserService:
    def get_all(self):
        users = User.query.filter_by(is_active=True).all()
        return users
    
    def create(self, data: CreateUserSchema):
        user = User(
            name=data.name,
            email=data.email,
            password=data.password,
            role_id=data.role_id
        )
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user: User, data: CreateUserSchema):
        user.name = data.name
        user.email = data.email
        user.role_id = data.role_id

        if data.password:
            user.password = data.password

        db.session.commit()
        return user

    def delete(self, user: User):
        user.is_active = False
        db.session.commit()
        return user
    
    def get_by_id(self, id: int) -> User | None:
        user = User.query.filter_by(id=id).first()
        return user

user_service = UserService()