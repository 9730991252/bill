# Generated by Django 5.0.6 on 2024-06-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0025_add_stock_parti_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_stock',
            name='disc_price',
            field=models.FloatField(null=True),
        ),
    ]
