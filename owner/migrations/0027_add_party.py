# Generated by Django 5.0.6 on 2024-06-14 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0026_add_stock_disc_price'),
        ('sunil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=200)),
                ('party_address', models.CharField(max_length=500)),
                ('license_number', models.CharField(max_length=20)),
                ('gst_number', models.CharField(max_length=50)),
                ('medical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.medical')),
            ],
        ),
    ]