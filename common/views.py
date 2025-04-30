from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from common.services.service import CommonService


def custom_404(request, exception):
    return render(request, '404.html', status=404)


class ReportView(View):
    def get(self, request):
        try:
            return CommonService.generate_report(request)
        except Exception as e:
            messages.error(request, f"Erro ao gerar o arquivo: {str(e)}")
            return redirect('dashboard')
