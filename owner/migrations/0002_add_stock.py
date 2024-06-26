# Generated by Django 5.0.6 on 2024-06-01 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
        ('sunil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('add_qty', models.IntegerField()),
                ('stock_qty', models.IntegerField()),
                ('expiry_date', models.DateField(null=True)),
                ('stock_status', models.IntegerField(choices=[('1', 'in stock'), ('0', 'out of stock'), ('2', 'cancel')], default=1)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.item')),
                ('medical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.medical')),
            ],
        ),
    ]
