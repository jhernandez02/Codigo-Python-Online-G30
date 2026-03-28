from app.models.role_model import Role
from app.schemas.role_schema import RoleSchema

class RoleService:
    def create(self, data: RoleSchema):
        Role(
            name=data.name
        )

role_service = RoleService()