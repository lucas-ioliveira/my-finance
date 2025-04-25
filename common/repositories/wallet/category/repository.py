from django.shortcuts import get_object_or_404

from wallet.models import Category


class CategoryRepository:

    @staticmethod
    def get_all(user):
        return Category.objects.all().filter(user=user, active=True)

    @staticmethod
    def get_all_by_search(user, search):
        return Category.objects.all().filter(user=user, active=True).filter(name__icontains=search)

    @staticmethod
    def create(user, name, description):
        Category.objects.create(
            user=user,
            name=name,
            description=description
        )

    @staticmethod
    def update(category_id, name, description):
        category = get_object_or_404(Category, id=category_id)
        category.name = name
        category.description = description
        category.save()

    @staticmethod
    def delete(category_id, active):
        category = get_object_or_404(Category, id=category_id)
        category.active = active
        category.save()
