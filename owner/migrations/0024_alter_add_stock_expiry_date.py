# Generated by Django 5.0.6 on 2024-06-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0023_alter_add_stock_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_stock',
            name='expiry_date',
            field=models.DateField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
