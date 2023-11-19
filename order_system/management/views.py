from django.shortcuts import render
from django.views import View
from django.utils.timezone import datetime
from customer.models import OrderModel

# Create your views here.

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        orders = OrderModel.objects.filter()
        return render(request, 'management/dashboard.html')
