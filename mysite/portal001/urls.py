from django.urls import path
from . import views

urlpatterns = [
    path('', views.curo, name='curo'),
    path('selectOrder/<orderno>', views.selectOrder, name='selectOrder'),
    path('updateOrder', views.updateOrder, name='updateOrder'),
    path('createOrder', views.createOrder, name='createOrder'),
    path('saveOrder', views.saveOrder, name='saveOrder'),
    path('searchOrders', views.searchOrders, name='searchOrders'),
    path('orderOrders', views.orderOrders, name='orderOrders'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('searchDashboard', views.searchDashboard, name='searchDashboard'),
    path('orderDashboard', views.orderDashboard, name='orderDashboard'),
]
