# Generated by Django 4.2.7 on 2023-11-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
