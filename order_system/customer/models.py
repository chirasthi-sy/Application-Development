from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import Group, User


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
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class OrderModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Order:{self.created_on.strftime("%b %d %I:%M %p")}'


@receiver(user_signed_up)
def assign_to_customer_group(sender, request, user, **kwargs):
    # Get or create the 'customer' group
    customer_group, created = Group.objects.get_or_create(name='customers')

    # Add the user to the 'customer' group
    user.groups.add(customer_group)

@receiver(post_save, sender=User)
def add_to_customer_group(sender, instance, created, **kwargs):
    if created:
        # Get or create the 'customer' group
        customer_group, created = Group.objects.get_or_create(name='customers')

        # Add the user to the 'customer' group
        instance.groups.add(customer_group)
