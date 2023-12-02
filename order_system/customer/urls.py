from django.urls import path
from .views import CustomerDashboard, OrderDetails

urlpatterns = [
    path('dashboard/', CustomerDashboard.as_view(), name='customer-dashboard'),
    path('order/<int:pk>/', OrderDetails.as_view(), name='cus_order_details'),

]