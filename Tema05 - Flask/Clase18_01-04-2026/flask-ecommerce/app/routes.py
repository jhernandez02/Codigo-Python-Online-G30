from flask_restful import Api
from app import app
from app.resources.user_resource import (
    UserResource,
    ManageUserResource
)
from app.resources.role_resource import RoleResource
from app.resources.auth_resource import (
    LoginResource,
    RegisterResource
)

api = Api(app, prefix='/api/v1')

api.add_resource(UserResource, '/users')
api.add_resource(ManageUserResource, '/users/<int:id>')

api.add_resource(LoginResource, '/auth/login')

api.add_resource(RoleResource, '/roles')
