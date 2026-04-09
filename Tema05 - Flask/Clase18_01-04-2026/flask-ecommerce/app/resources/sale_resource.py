from flask_restful import Resource
from flask import request
from app.schemas.sale_schema import SaleSchema
from app.services.sale_service import sale_service

class SaleResource(Resource):
    def get(self):
        try:
            sales = sale_service.get_all()

            sales_list = []
            for sale in sales:
                sales_list.append(sale.to_json())

            return sales_list, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        try:
            json = request.get_json()
            validated_data = SaleSchema.model_validate(json)
            
            sale = sale_service.create(validated_data)

            return sale.to_json(), 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400