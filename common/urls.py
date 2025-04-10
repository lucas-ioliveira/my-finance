from django.urls import path
from common.views import ReportView

urlpatterns = [
    path('', ReportView.as_view(), name='report'),
]
