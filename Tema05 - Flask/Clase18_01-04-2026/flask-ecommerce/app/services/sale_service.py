from app.models.sale_model import Sale
from app.schemas.sale_schema import SaleSchema
from app.models.product_model import Product
from app.models.sale_detail_model import SaleDetail
from app.models.customer_model import Customer
from db import db

class SaleService:
    def get_all(self) -> list[Sale]:
        sales = Sale.query.all()
        return sales
    
    def create(self, data: SaleSchema) -> Sale:
        new_sale_details = []
        for detail in data.sale_details:
            product = Product.query.get(detail.product_id)

            if not product:
                raise ValueError('Product not found')
            if not product.is_active:
                raise ValueError(f'Product {product.name} is not active')
            if product.stock < detail.quantity:
                raise ValueError(f'Not enough stock for {product.name}')
            
            product.stock -= detail.quantity

            new_detail = SaleDetail(
                quantity=detail.quantity,
                price=product.price,
                subtotal=product.price * detail.quantity,
                product_id=detail.product_id
            )
            new_sale_details.append(new_detail)

        customer = Customer.query.filter_by(
            document_number=data.customer.document_number
        ).first()

        if not customer:
            customer = Customer(
                name=data.customer.name,
                last_name=data.customer.last_name,
                email=data.customer.email,
                document_number=data.customer.document_number,
                address=data.customer.address
            )
            db.session.add(customer)
        else:
            customer.name = data.customer.name
            customer.last_name = data.customer.last_name
            customer.email = data.customer.email
            customer.address = data.customer.address

        db.session.flush()

        last_sale = Sale.query.order_by(
            Sale.id.desc()
        ).first()
        new_code = 'B-0001'
        if last_sale:
            code = last_sale.code
            new_code = 'B-' + str(int(code.split('-')[1]) + 1).zfill(4)
        
        sale = Sale(
            code=new_code,
            total=data.total,
            customer_id=customer.id,
            sale_details=new_sale_details,
            status='PENDING'
        )

        db.session.add(sale)
        db.session.commit()
        return sale
    

sale_service = SaleService()