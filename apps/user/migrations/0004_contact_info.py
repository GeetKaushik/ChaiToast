# Generated by Django 5.0.2 on 2024-02-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_product_description_alter_product_image_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.EmailField(max_length=254)),
                ('u_message', models.CharField(max_length=200)),
            ],
        ),
    ]