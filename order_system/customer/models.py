from django.db import models
# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
       return self.name

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)

    name = models.CharField(max_length=100, blank=True)
    number = models.DecimalField(max_digits=10, decimal_places=0, default=000)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_time = models.TimeField(blank=True, null=True)
    special_notes = models.CharField(max_length=350, blank=True)
    payment_option_choices = [('cash', 'Cash on Delivery')]
    payment_option = models.CharField(max_length=10, choices=payment_option_choices, default='cash')
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order:{self.created_on.strftime("%b %d %I:%M %p")}'
       




