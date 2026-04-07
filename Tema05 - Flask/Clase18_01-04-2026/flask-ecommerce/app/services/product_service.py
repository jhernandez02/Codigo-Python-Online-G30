from app.models.product_model import Product
from app.schemas.product_schema import ProductSchema
from db import db


class ProductService:
    def get_all(self):
        products = Product.query.filter_by(
            is_active=True
        )
        return products
    
    def create(self, data: ProductSchema) -> Product:
        product = Product(
            name=data.name,
            code='',
            description=data.description,
            image='',
            brand=data.brand,
            size=data.size,
            price=data.price,
            stock=data.stock,
            category_id=data.category_id
        )
        db.session.add(product)
        db.session.commit()
        return product


product_service = ProductService()