from django.shortcuts import render
from django.views import View

class Index(View):
    def get(selfself,request.*args,**kwargs):
        return render(request,'customer/index.html')

class About(View):
    def get(selfself, request,*args, ** kwargs):
        return render(request, 'customer/about.html')

# Create your views here.
