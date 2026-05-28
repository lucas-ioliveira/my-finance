from easyaudit.models import CRUDEvent


class CommonRepository:
    
    @staticmethod
    def get_recent_creates(user, limit=5):
        return CRUDEvent.objects.filter(
            user=user, 
            event_type=CRUDEvent.CREATE
        ).order_by('-datetime')[:limit]

    @staticmethod
    def get_recent_updates(user, limit=5):
        return CRUDEvent.objects.filter(
            user=user, 
            event_type=CRUDEvent.UPDATE
        ).order_by('-datetime')[:limit]

    @staticmethod
    def get_recent_deletes(user, limit=5):
        return CRUDEvent.objects.filter(
            user=user, 
            event_type=CRUDEvent.DELETE
        ).order_by('-datetime')[:limit]
