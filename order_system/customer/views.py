from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/Home_page.html')

class About(View):
    def get(self, request,*args, **kwargs):
        return render(request, 'customer/about_us.html')

class Order(View):
    def get(self,request,*args,**kwargs):

#get every item from each category
#pass into context

#render the template
# Create your views here.
