from django.core.paginator import Paginator


from common.repositories.base.base_repository import BaseRepository


class BaseService:
    def __init__(self, model):
        self.model = model

    def get_all(self, request):
        user = request.user
        search = request.GET.get('search')
        page = request.GET.get('page')
        if search:
            queryset = BaseRepository.get_all_by_search(user, search)
        else:
            queryset = BaseRepository.get_all(self, user)

        paginator = Paginator(queryset, 6)
        return paginator.get_page(page)

    def delete(self, object_id):
        active = False
        BaseRepository.delete(self, object_id, active)
