from flask_restful import Resource
from app.services.user_service import user_service

class UserResource(Resource):
    def get(self):
        try:
            users = user_service.get_all()
            return users, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        pass

class ManageUserResource(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass