from django.urls import path
from . import views

urlpatterns = [
    path('customers/<int:customer_id>/contracts/', views.ContractList.as_view(), name='contract-list'),
    path('customers/<int:customer_id>/contracts/<int:contract_id>/', views.ContractDetail.as_view(),
         name='contract-detail'),
]
