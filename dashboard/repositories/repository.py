from easyaudit.models import CRUDEvent


class DashboardRepository:
    @staticmethod
    def get_crud_events(user):
        create = CRUDEvent.objects.filter(user=user, event_type=CRUDEvent.CREATE).order_by('-datetime')[:5]
        update = CRUDEvent.objects.filter(user=user, event_type=CRUDEvent.UPDATE).order_by('-datetime')[:5]
        delete = CRUDEvent.objects.filter(user=user, event_type=CRUDEvent.DELETE).order_by('-datetime')[:5]
        combined = list(create) + list(update) + list(delete)

        return sorted(combined, key=lambda x: x.datetime, reverse=True)[:3]
