# Generated by Django 4.1.7 on 2023-08-29 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_car_delete_email_order_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
