# Generated by Django 5.0.2 on 2024-02-23 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.DeleteModel(
            name='Kitchen',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]
