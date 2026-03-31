from flask_restful import Resource
from flask import request
from pydantic import ValidationError
from app.services.user_service import user_service
from app.schemas.user_schema import (
    CreateUserSchema,
    UpdateUserSchema
)
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
                users_list.append(user.to_json())
            return users_list, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        try:
            json = request.get_json()
            validated_data = CreateUserSchema.model_validate(json)
            validated_data.password = hash_password(validated_data.password)
            user = user_service.create(validated_data)

            return user.to_json(), 200
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
        try:
            user = user_service.get_by_id(id)

            if not user:
                return {
                    'error': 'User not found'
                }, 404

            return user.to_json(), 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def put(self, id):
        try:
            json = request.get_json()
            validated_data = UpdateUserSchema.model_validate(json)

            user = user_service.get_by_id(id)

            if not user:
                return {
                    'error': 'User not found'
                }, 404
            
            if validated_data.password:
                validated_data.password = hash_password(validated_data.password)
            
            user = user_service.update(user, validated_data)

            return user.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def delete(self, id):
        try:
            user = user_service.get_by_id(id)

            if not user:
                return {
                    'error': 'User not found'
                }, 404
            
            user_service.delete(user)

            return '', 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400