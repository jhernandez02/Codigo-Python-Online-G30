from flask_restful import Resource
from flask import request
from pydantic import ValidationError
from app.services.user_service import user_service
from app.schemas.user_schema import UserSchema
import bcrypt

def hash_password(password: str) -> str:
    bytes_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(
        bytes_password,
        bcrypt.gensalt()
    )
    return hashed_password.decode('utf-8')

class UserResource(Resource):
    def get(self):
        try:
            users = user_service.get_all()
            users_list = []
            for user in users:
                users_list.append({
                    'id': user.id,
                    'name': user.name,
                    'email': user.email
                })
            return users_list, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        try:
            json = request.get_json()
            validated_data = UserSchema.model_validate(json)
            validated_data.password = hash_password(validated_data.password)
            user = user_service.create(validated_data)

            return {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role_id': user.role_id
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400

class ManageUserResource(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass