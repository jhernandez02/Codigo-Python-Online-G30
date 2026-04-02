from pydantic import BaseModel
from typing import Optional

class BaseUserSchema(BaseModel):
    name: str
    last_name: str
    email: str
    role_id: int

class CreateUserSchema(BaseUserSchema):
    password: str

class UpdateUserSchema(BaseUserSchema):
    password: Optional[str] = None
