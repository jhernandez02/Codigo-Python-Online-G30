from app.models.product_model import Product
from app.schemas.product_schema import ProductSchema
from db import db


class ProductService:
    def get_all(self):
        products = Product.query.filter_by(
            is_active=True
        )
        return products
    
    def create(
            self,
            data: ProductSchema,
            code: str,
            image: str
        ) -> Product:
        product = Product(
            name=data.name,
            code=code,
            description=data.description,
            image=image,
            brand=data.brand,
            size=data.size,
            price=data.price,
            stock=data.stock,
            category_id=data.category_id
        )
        db.session.add(product)
        db.session.commit()
        return product
    
    def get_last(self) -> Product | None:
        product = Product.query.order_by(
            Product.id.desc()
        ).first()
        return product


product_service = ProductService()