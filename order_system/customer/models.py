from django.db import models
class MenuItem(models.model):
    name=models.CharField(max_length=100)
    description=model.TextField()
    image=models.ImageField(upload_to='menu_images/')
    price=model.DecimalField(max_digits=5,decimal_places=2)
    category=models.ManyToManyField('Category',related_name='item')

    def__str__(self):
       return self.name
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderModel(model.model):
    created_on=models.DateTimeField(auto_now_add=True)
    price=modls.DecimalField(max_digits=7,decimal_places=2)
        "# Create your models here.
