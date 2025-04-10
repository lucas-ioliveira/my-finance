from django.urls import path
from wallet.views import (
    CategoryView, CategoryDeleteView, CategoryEditView,
    RevenueView, RevenueEditView, RevenueDeleteView, RevenueCloneView,
    ExpenseView, ExpenseDeleteView, ExpenseEditView, ExpenseCloneView,
    InvestmentsView, InvestmentsEditView, InvestmentsDeleteView, InvestmentsCloneView
)


urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('category/edit/<int:category_id>/', CategoryEditView.as_view(), name='category-edit'),
    path('category/delete/<int:category_id>/', CategoryDeleteView.as_view(), name='category-delete'),

    path('revenue/', RevenueView.as_view(), name='revenue'),
    path('revenue/delete/<int:revenue_id>/', RevenueDeleteView.as_view(), name='revenue-delete'),
    path('revenue/edit/<int:revenue_id>/', RevenueEditView.as_view(), name='revenue-edit'),
    path('revenue/clone/<int:revenue_id>/', RevenueCloneView.as_view(), name='revenue-clone'),

    path('expense/', ExpenseView.as_view(), name='expense'),
    path('expense/delete/<int:expense_id>/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('expense/edit/<int:expense_id>/', ExpenseEditView.as_view(), name='expense-edit'),
    path('expense/clone/<int:expense_id>/', ExpenseCloneView.as_view(), name='expense-clone'),

    path('investments/', InvestmentsView.as_view(), name='investments'),
    path('investments/delete/<int:investments_id>/', InvestmentsDeleteView.as_view(), name='investments-delete'),
    path('investments/edit/<int:investments_id>/', InvestmentsEditView.as_view(), name='investments-edit'),
    path('investments/clone/<int:investments_id>/', InvestmentsCloneView.as_view(), name='investments-clone'),
]
