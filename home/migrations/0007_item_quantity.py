# Generated by Django 4.1.7 on 2023-08-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_item_is_retired'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
