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
from app.resources.category_resource import CategoryResource
from app.resources.product_resource import (
    ProductResource,
    ManageProductResource
)

api = Api(app, prefix='/api')

api.add_resource(UserResource, '/users')
api.add_resource(ManageUserResource, '/users/<int:id>')

api.add_resource(LoginResource, '/auth/login')

api.add_resource(RoleResource, '/roles')

api.add_resource(CategoryResource, '/categories')
api.add_resource(ProductResource, '/products')
api.add_resource(ManageProductResource, '/products/<int:id>')