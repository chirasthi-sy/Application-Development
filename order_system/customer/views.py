from django.shortcuts import render
from django.views import View

class Index(View):
    def get(selfself,request,*args,**kwargs):
        return render(request,'customer/index.html')

class About(View):
    def get(selfself, request,*args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(selfself,request,*args,**kwargs):

        #get every item from each category
#pass into context

#render the template



# Create your views here.
