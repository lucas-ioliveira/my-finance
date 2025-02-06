from django.urls import path
from wallet.views import RevenueView, CategoryView, CategoryDeleteView, CategoryEditView

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('category/edit/<int:category_id>/', CategoryEditView.as_view(), name='category-edit'),
    path('category/delete/<int:category_id>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('revenue/', RevenueView.as_view(), name='revenue'),
]
