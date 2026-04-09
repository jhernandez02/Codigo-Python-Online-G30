from pydantic import BaseModel, Field

class CustomerSchema(BaseModel):
    name: str = Field(..., description='Nombre del cliente', max_length=255)
    last_name: str = Field(..., description='Apellido del cliente', max_length=255)
    email: str = Field(..., description='Email del cliente', max_length=255)
    document_number: str = Field(..., description='Numero de documento del cliente', max_length=255)
    address: str = Field(..., description='Direccion del cliente' , max_length=255)

class SaleDetailSchema(BaseModel):
    quantity: int = Field(..., description='Cantidad de productos')
    price: float = Field(..., description='Precio de cada producto', ge=0, le=10000)
    subtotal: float = Field(..., description='Subtotal de la venta', ge=0, le=10000)
    product_id: int = Field(..., description='Id del producto')

class SaleSchema(BaseModel):
    total: float = Field(..., description='Total de la venta')
    customer: CustomerSchema
    sale_details: list[SaleDetailSchema]