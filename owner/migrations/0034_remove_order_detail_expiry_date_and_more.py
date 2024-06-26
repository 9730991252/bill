# Generated by Django 5.0.6 on 2024-06-16 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0033_add_stock_schedule_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_detail',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='order_detail',
            name='invice_number',
        ),
        migrations.RemoveField(
            model_name='order_detail',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='order_detail',
            name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.item'),
        ),
        migrations.AddField(
            model_name='order_detail',
            name='add_stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.add_stock'),
        ),
        migrations.AddField(
            model_name='order_detail',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.doctor'),
        ),
        migrations.AddField(
            model_name='order_detail',
            name='sell_price_per_unit',
            field=models.FloatField(null=True),
        ),
    ]
