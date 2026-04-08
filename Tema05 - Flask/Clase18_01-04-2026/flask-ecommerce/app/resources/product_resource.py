from flask_restful import Resource
from flask import request
from app.schemas.product_schema import ProductSchema
from pydantic import ValidationError
from app.utils.helpers import cloudinary_helper
from app.services.product_service import product_service
from db import db

class ProductResource(Resource):
    def get(self):
        try:
            products = product_service.get_all()

            products_list = []
            for product in products:
                products_list.append(product.to_json())

            return products_list, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        try:
            form_data = request.form.to_dict()
            validated_data = ProductSchema.model_validate(form_data)
            
            if 'image' not in request.files:
                return {
                    'error': 'Image is required'
                }, 400
            
            image = request.files['image']
            
            if image.filename == '':
                return {
                    'error': 'Image not found'
                }, 400
            
            if not image.content_type.startswith('image/'):
                return {
                    'error': 'Invalid image type'
                }, 400

            secure_url, public_id = cloudinary_helper.upload_image(image, 'products')

            if not secure_url:
                return {
                    'error': 'Error uploading image'
                }, 400
            
            next_code ='P-0001'
            product = product_service.get_last()
            if product:
                code = product.code
                next_code = 'P-' + str(int(code.split('-')[1]) + 1).zfill(4)
            
            product = product_service.create(
                validated_data,
                next_code,
                public_id
            )

            return product.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'error': str(e)
            }, 400

class ManageProductResource(Resource):
    def get(self, id: int):
        try:
            product = product_service.get_by_id(id)
            if not product:
                return {
                    'error': 'Product not found'
                }, 404
            
            return product.to_json(), 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def put(self, id: int):
        try:
            form_data = request.form.to_dict()
            validated_data = ProductSchema.model_validate(form_data)

            product = product_service.get_by_id(id)
            if not product:
                return {
                    'error': 'Product not found'
                }, 404
            
            image = request.files['image']

            if image:
                if image.filename == '':
                    return {
                        'error': 'Image not found'
                    }, 400
                
                if not image.content_type.startswith('image/'):
                    return {
                        'error': 'Invalid image type'
                    }
                
                secure_url, public_id = cloudinary_helper.upload_image(
                    image,
                    'products'
                )
                cloudinary_helper.delete_image(product.image)
                
                if not secure_url:
                    return {
                        'error': 'Error uploading image'
                    }, 400
            
            product = product_service.update(
                product,
                validated_data,
                public_id
            )

            return product.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'error': str(e)
            }, 400

    def delete(self, id: int):
        try:
            product = product_service.get_by_id(id)
            if not product:
                return {
                    'error': 'Product not found'
                }, 404
            
            product_service.delete(product)
            
            return None, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400