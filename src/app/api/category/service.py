from app.api.category.repository import CategoryRepository
from app.schema.categories import CreateCategory


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def get_all_categories(self):
        return self.category_repository.get_all_categories()

    def create_category(self, category: CreateCategory):
        return self.category_repository.create_category(category)
