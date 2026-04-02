from flask_restful import Resource
from app.services.category_service import category_service

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
        pass

class ManageCategoryResource(Resource):
    def get(self, id: int):
        pass

    def put(self, id: int):
        pass

    def delete(self, id: int):
        pass