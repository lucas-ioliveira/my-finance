from django.urls import path
from common.views import ReportView, RecentActivities

urlpatterns = [
    path('', ReportView.as_view(), name='report'),
    path('recent_activities/', RecentActivities.as_view(), name='recent_activities'),

]
