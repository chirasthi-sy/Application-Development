from django.shortcuts import render,redirect
from django.views import View
from django.core.mail import send_mail
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

        return render(request,"customer/menu.html", context)

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
            price=0
            item_ids=[]

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

        #after  everything is done, send confirmatin email to the user
        body=("Thank you for your order!Your food is being made and will be deliveerd soon \n"
         f'Your Total:{price}\n'
        'Thank you again for your order!')


        send_mail(
            'Thank You For Your Order!'
            'body,'
            'sponge@company.com',
            [email],
            fail_silently=False
        )

        context = {
            'items': order_items['items'],
            'price': price
        }
        return render(request, 'customer/order confirmation message.html', context)



#class OrderConfirmationView(View):
#    order = OrderModel.objects.get(pk=pk)

#    def get(self, request, pk, *args, **kwargs):
#        context = {
#            'pk': order.pk,
#            'items': order.items,
#            'price': order.price,
#        }
#        return render(request, 'customer/order_confirmation.html', context)







