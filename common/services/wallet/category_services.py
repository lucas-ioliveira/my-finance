from django.core.paginator import Paginator

from common.repositories.wallet.category_repository import CategoryRepository


class CategoryService:

    @staticmethod
    def get_all(request):
        user = request.user
        search = request.GET.get('search')
        page = request.GET.get('page')
        if search:
            queryset = CategoryRepository.get_all_by_search(user, search)
        else:
            queryset = CategoryRepository.get_all(user)

        paginator = Paginator(queryset, 6)
        return paginator.get_page(page)

    @staticmethod
    def create(request):
        user = request.user
        name = request.POST.get('name')
        description = request.POST.get('description')
        CategoryRepository.create(user, name, description)

    @staticmethod
    def update(request, category_id):
        name = request.POST.get('name_edit')
        description = request.POST.get('description_edit')
        CategoryRepository.update(category_id, name, description)

    @staticmethod
    def delete(category_id):
        active = False
        CategoryRepository.delete(category_id, active)
