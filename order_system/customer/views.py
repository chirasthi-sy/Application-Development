from django.shortcuts import render
from django.views import View
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
            'Whole Cakes': whole_cakes,
            'Dessert Platters': dessert_platters,
            'Cake Slices': cake_slices,
        }

        return render(request,"customer/menu.html", context)

def post(self, request, *args, **kwargs):

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

    order = OrderModel.objects.create(price=price)
    order.items.add(*item_ids)
    context = {
        'items': order_items['items'],
        'price': price
    }
    return render(request,'order confirmation message.html', context)








