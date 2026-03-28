from flask_restful import Resource
from flask import request
from app.schemas.role_schema import RoleSchema
from app.services.role_service import role_service

class RoleResource(Resource):
    def post(self):
        try:
            json = request.get_json()
            validated_data = RoleSchema.model_validate(json)
            role_service.create(validated_data)

            return 'Ok'
        except Exception as e:
            return {
                'error': str(e)
            }