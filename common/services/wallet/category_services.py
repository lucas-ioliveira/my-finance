from common.services.base.base_services import BaseService
from common.repositories.wallet.category_repository import CategoryRepository
from wallet.models import Category


class CategoryService(BaseService):
    def __init__(self):
        super().__init__(Category)
        self.repository = CategoryRepository()

    def create(self, request):
        user = request.user
        name = request.POST.get('name')
        description = request.POST.get('description')
        self.repository.create(user, name, description)

    def update(self, request, category_id):
        name = request.POST.get('name_edit')
        description = request.POST.get('description_edit')
        self.repository.update(category_id, name, description)
