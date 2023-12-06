from django.urls import path
from .views import CustomerDashboard, OrderDetails

#This creates the URL s to display the customer dashboard and order details
urlpatterns = [
    path('dashboard/', CustomerDashboard.as_view(), name='customer-dashboard'),
    path('order/<int:pk>/', OrderDetails.as_view(), name='cus_order_details'),

]