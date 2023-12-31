# Generated by Django 4.2.7 on 2023-11-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_menuitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='delivery_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='number',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='payment_option',
            field=models.CharField(choices=[('cash', 'Cash on Delivery')], default='cash', max_length=10),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='special_notes',
            field=models.CharField(blank=True, max_length=350),
        ),
    ]
