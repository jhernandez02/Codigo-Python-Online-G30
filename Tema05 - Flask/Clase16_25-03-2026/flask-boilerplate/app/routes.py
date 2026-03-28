from flask_restful import Api
from app import app
from app.resources.user_resource import (
    UserResource,
    ManageUserResource
)
from app.resources.role_resource import RoleResource

api = Api(app, prefix='/api/v1')

api.add_resource(UserResource, '/users')
api.add_resource(ManageUserResource, '/users/<int:id>')

api.add_resource(RoleResource, '/roles')