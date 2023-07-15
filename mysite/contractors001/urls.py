from django.urls import path
from . import views

urlpatterns = [
    path('', views.curoContractors, name='curoContractors'),
    path('searchContractors', views.searchContractors, name='searchContractors'),
    path('orderContractors', views.orderContractors, name='orderContractors'),
]
