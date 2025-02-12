from wallet.models import Revenue, Expense, Investments


class Dashboard:

    @staticmethod
    def  get_recent_transactions():
        revenue = Revenue.objects.all().order_by('-created_at')[:5]
        expense = Expense.objects.all().order_by('-created_at')[:5]
        investments = Investments.objects.all().order_by('-created_at')[:5]
        combined = list(revenue) + list(expense) + list(investments)
        
        return sorted(combined, key=lambda x: x.created_at, reverse=True)