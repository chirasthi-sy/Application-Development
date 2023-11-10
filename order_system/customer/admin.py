from django.contrib import admin
from .models import MenuItem,Category,OrderModel
# Register your models here.l

from .models import Category

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(OrderModel)

