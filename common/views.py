from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from common.services.service import CommonService
from common.repositories.repository import CommonRepository


def custom_404(request, exception):
    return render(request, '404.html', status=404)


class ReportView(View):
    def get(self, request):
        try:
            return CommonService.generate_report(request)
        except Exception as e:
            messages.error(request, f"Erro ao gerar o arquivo: {str(e)}")
            return redirect('dashboard')


class RecentActivities(View):
    def get(self, request):

        recent_creates = CommonRepository.get_recent_creates(request.user)
        recent_updates = CommonRepository.get_recent_updates(request.user)
        recent_deletes = CommonRepository.get_recent_deletes(request.user)

        context = {
            'recent_creates': recent_creates,
            'recent_updates': recent_updates,
            'recent_deletes': recent_deletes
        }
        return render(request, 'recent_activities/recent_activities.html', context)
