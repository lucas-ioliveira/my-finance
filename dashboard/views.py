from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum

from datetime import datetime, timedelta

from wallet.models import Revenue

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        data_limite = datetime.now() - timedelta(days=30)

        revenues_total = Revenue.objects.filter(user=request.user, active=True, created_at__gte=data_limite).aggregate(total_revenues=Sum('amount'))
        
        context = {
            'revenues_total': revenues_total['total_revenues']
        }
        return render(request, 'dashboard.html', context)
