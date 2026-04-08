from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=255, description='Nombre del producto')
    description: str = Field(..., min_length=2, max_length=255, description='Descripcion del producto')
    brand: str
    size: str
    price: float = Field(..., gt=0, description='El precio debe ser estrictamente mayor a 0')
    stock: int = Field(default=0, ge=0, description='El stock no puede ser negativo')
    category_id: int