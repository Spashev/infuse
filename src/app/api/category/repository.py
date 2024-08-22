from sqlalchemy.orm import Session

from app.database.models.categories import Category as CategoryModel
from app.schema.categories import CreateCategory


class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_categories(self):
        return self.session.query(CategoryModel).all()

    def create_category(self, category: CreateCategory):
        category_model = CategoryModel(**category.dict())
        self.session.add(category_model)
        self.session.commit()
        self.session.refresh(category_model)
        return category_model
