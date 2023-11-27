from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import MenuItem, Category, OrderModel


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/Home_page.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about_us.html')






class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/contact_us.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        whole_cakes = MenuItem.objects.filter(category__name__contains="Whole Cakes")
        dessert_platters = MenuItem.objects.filter(category__name__contains="Dessert Platters")
        cake_slices = MenuItem.objects.filter(category__name__contains="Cake Slices")

        context = {
            'WholeCakes': whole_cakes,
            'DessertPlatters': dessert_platters,
            'CakeSlices': cake_slices,
        }

        return render(request, "customer/menu.html", context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('customer_name')
        number = request.POST.get('contact_number')
        email = request.POST.get('email')
        address = request.POST.get('delivery_address')
        delivery_date = request.POST.get('delivery_date')
        delivery_time = request.POST.get('delivery_time')
        special_notes = request.POST.get('special_notes')
        payment_option = request.POST.get('payment_option')

        order_items = {
            'items': []
        }

        items = request.POST.getlist("items[]")
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price

            }

            order_items['items'].append(item_data)
            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            number=number,
            email=email,
            address=address,
            delivery_date=delivery_date,
            delivery_time=delivery_time,
            special_notes=special_notes,
            payment_option=payment_option
        )
        order.items.add(*item_ids)

        body = (
            f"Thank you for your order! Your cake will be delivered on {delivery_date}.\n Your total is {price}. \n "
            f"We appreciate your business!")

        # This will display an email in the console
        send_mail('Thank You For Your Order!', body, "info@sponge.lk", [email], fail_silently=False)

        context = {
            'items': order_items['items'],
            'price': price
        }
        return redirect('order-confirmation', pk=order.pk)
        # return render(request, 'customer/order confirmation message.html', context)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }
        return render(request, 'customer/order confirmation message.html', context)


class CustomerDashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        orders = OrderModel.objects.filter(user=user)

        context = {
            'orders': orders,
            'total_orders': len(orders)
        }
        return render(request, 'customer/customer dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='customers').exists()


class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {
            'order': order
        }
        return render(request, 'customer/order-details.html', context)

    def post(self, request, pk, *args, **kwargs):
        # Assuming you want to update the order status or perform some action
        order = OrderModel.objects.get(pk=pk)
        # Add your logic here to update the order status or perform other actions

        context = {
            "order": order
        }
        return render(request, "customer/order-details.html", context)

    def test_func(self):
        return self.request.user.groups.filter(name='customers').exists()