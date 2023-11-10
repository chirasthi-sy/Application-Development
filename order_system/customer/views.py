from django.shortcuts import render
from django.views import View

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
        #change this first chirasthi

        appetizers=MenuItem.objetcs.filter(category__name__contains="Appertizer")
        entres = MenuItem.objetcs.filter(category__name__contains="Entre")
        desserts = MenuItem.objetcs.filter(category__name__contains="Dessert")
        drinks= MenuItem.objetcs.filter(category__name__contains="Drink")

        context={
            'appertizers': appertizers,
            'entres':entres,
            'desserts':desserts,
             "drinks":drinks,
        }

        #render the template
        return render(request,"customer/order.html",context)

def post(self,requset,*args,**kwargs)

    order_items={
        'items':[]
    }
    items=request.POST.getlist("items[]")
    for item in items:
        menu_item=MenuItem.objects.get(pk__contains=int(item))
        item_data={
            'id':menu_item.pk,
            'name':menu_item.name,
            'price':menu_item.price

        }

        order_items['items'].append(item_data)
        price=0
        item_ids=[]

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order=OrderModel.objects.create(price=price)
        order.items.add(*item_id)
        context={
            'items':order_items['items'],
            'price':price
        }
        return render(request,'customer/order_confirmation.html',context)

        order=OrderModel.objects.create(price=price)





#get every item from each category
#pass into context

#render the template
# Create your views here.
