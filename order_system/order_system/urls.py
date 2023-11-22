"""
URL configuration for order_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from customer.views import Index, About, Contact, Order, OrderConfirmation, custom_profile_view
from django.conf import settings
from django.conf.urls.static import static

#created url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', custom_profile_view, name='custom_profile_view'),
    path('management/', include('management.urls')),
    path('', Index.as_view(),name='home'),
    path('about/', About.as_view(),name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('menu/', Order.as_view(), name='order'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name='order-confirmation')
    path('dashboard/', CustomerDashboard.as_view(), name='customer_dashboard'),
    path('order/<int:pk>/', OrderDetails.as_view(), name='order_details'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)