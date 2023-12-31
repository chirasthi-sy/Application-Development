from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel


# Create your views here.
# This view displays the management dashboard for a logged in employee
class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):

    # This method filters al the orders for the day
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        # These loops calculate the total revenue and total orders for the day
        unshipped_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

            if not order.is_shipped:
                unshipped_orders.append(order)

        context = {
            'orders': unshipped_orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }
        return render(request, 'management/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='staff').exists()


# This view displays the order details of the orders for the logged in employee
class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {
            'order': order

        }
        return render(request, 'management/order-details.html', context)

    # This method posts the shipping and payment status once the order is completed
    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.is_shipped = True
        order.is_paid = True
        order.save()

        context = {
            "order": order
        }
        return render(request, "restaurant/order-details.html", context)

    def test_func(self):
        return self.request.user.groups.filter(name='staff').exists()
