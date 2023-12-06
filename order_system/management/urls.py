from django.urls import path
from .views import Dashboard, OrderDetails
#This creates the url patterns for the managemnet dashboard and order details view
urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path("orders/<int:pk>/", OrderDetails.as_view(), name='order-details'),

]


