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
    path('dashboard/<guage>', views.dashboard, name='dashboard'),
    path('searchDashboard/<guage>', views.searchDashboard, name='searchDashboard'),
    path('orderDashboard/<guage>', views.orderDashboard, name='orderDashboard'),
    path('selectNotification/<orderno>', views.selectNotification,
         name='selectNotification'),
]
