# Generated by Django 5.0.2 on 2024-02-23 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0002_remove_sale_product_delete_kitchen_delete_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, unique=True)),
                ('product_description', models.CharField(max_length=500)),
                ('product_image', models.ImageField(upload_to='kitchen/')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.kitchen')),
            ],
        ),
    ]