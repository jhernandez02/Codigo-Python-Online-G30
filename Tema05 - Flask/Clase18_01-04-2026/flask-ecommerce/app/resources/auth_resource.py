from flask_restful import Resource
from flask import request
from app.schemas.auth_schema import LoginSchema
from app.services.user_service import user_service
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
)
import bcrypt
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def verify_password(password: str, hashed_password: str) -> bool:
    bytes_password = password.encode('utf-8')
    bytes_hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(
        bytes_password,
        bytes_hashed_password
    )

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = user_service.get_by_id(user_id)
            if not user:
                return {
                    'error': 'User not found'
                }, 401

            if user.role.name != 'ADMIN':
                return {
                    'error': 'User not authorized'
                }, 403
            
            return fn(*args, **kwargs)
        return decorator
    return wrapper


class LoginResource(Resource):
    def post(self):
        try:
            json = request.get_json()
            validated_data = LoginSchema.model_validate(json)

            user = user_service.get_by_email(validated_data.email)

            if not user:
                return {
                    'error': 'Email not found'
                }, 401
            
            is_password_valid = verify_password(
                validated_data.password,
                user.password
            )

            if not is_password_valid:
                return {
                    'error': 'Invalid password'
                }, 401
            
            access_token = create_access_token(
                identity=str(user.id),
                additional_claims={
                    'name': user.name,
                    'last_name': user.last_name,
                    'email': user.email
                }
            )
            refresh_token = create_refresh_token(
                identity=str(user.id)
            )
            
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
class RegisterResource(Resource):
    pass