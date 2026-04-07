from flask_restful import Resource
from flask import request
from app.schemas.product_schema import ProductSchema
from pydantic import ValidationError
from app.utils.helpers import cloudinary_helper
from app.services.product_service import product_service

class ProductResource(Resource):
    def get(self):
        try:
            pass
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
            
            product = product_service.create(validated_data)

            return 'Ok', 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400

class ManageProductResource(Resource):
    def get(self, id: int):
        pass

    def put(self, id: int):
        pass

    def delete(self, id: int):
        pass