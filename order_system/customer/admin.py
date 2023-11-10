from django.contrib import admin
from .models import Menuitem,Category,OrderModel
# Register your models here.

from .models import Category

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(OrderModel)

