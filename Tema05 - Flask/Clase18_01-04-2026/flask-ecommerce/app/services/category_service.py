from app.models.category_model import Category

class CategoryService:
    def get_all(self) -> list[Category]:
        categories = Category.query.filter_by(is_active=True).all()
        return categories
    

category_service = CategoryService()