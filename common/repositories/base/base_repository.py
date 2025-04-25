from django.shortcuts import get_object_or_404


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self, user):
        return self.model.objects.all().filter(user=user, active=True)

    def get_all_by_search(self, user, search):
        return self.model.objects.all().filter(user=user, active=True).filter(name__icontains=search)

    def delete(self, object_id, active):
        object = get_object_or_404(self.model, id=object_id)
        object.active = active
        object.save()
