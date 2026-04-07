from flask_restful import Resource
from flask import request
from app.services.category_service import category_service
from pydantic import ValidationError
from app.schemas.category_schema import CategorySchema

class CategoryResource(Resource):
    def get(self):
        try:
            categories = category_service.get_all()
            categories_list = []
            for category in categories:
                categories_list.append(
                    category.to_json()
                )

            return categories_list, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        try:
            json = request.get_json()
            validated_data = CategorySchema.model_validate(json)
            category = category_service.create(validated_data)
            return category.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400

class ManageCategoryResource(Resource):
    def get(self, id: int):
        try:
            category = category_service.get_by_id(id)
            if not category:
                return {
                    'error': 'Category not found'
                }, 404
            
            return category.to_json(), 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def put(self, id: int):
        try:
            json = request.get()
            validated_data = CategorySchema.model_validate(json)
            
            category = category_service.get_by_id(id)
            
            if not category:
                return {
                    'error': 'Category not found'
                }, 404
            
            category = category_service.update(
                category,
                validated_data
            )
            return category.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def delete(self, id: int):
        try:
            category = category_service.get_by_id(id)

            if not category:
                return {
                    'error': 'Category not found'
                }, 404
            
            category_service.delete(category)

            return None, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400