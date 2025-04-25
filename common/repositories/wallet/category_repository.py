from django.shortcuts import get_object_or_404

from common.repositories.base.base_repository import BaseRepository
from wallet.models import Category


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)

    def create(self, user, name, description):
        self.model.objects.create(
            user=user,
            name=name,
            description=description
        )

    def update(self, category_id, name, description):
        category = get_object_or_404(Category, id=category_id)
        category.name = name
        category.description = description
        category.save()

    def delete(self, category_id, active):
        category = get_object_or_404(Category, id=category_id)
        category.active = active
        category.save()
