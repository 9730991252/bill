# Generated by Django 5.0.6 on 2024-06-10 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0020_item_item_type_alter_add_stock_expiry_date'),
        ('sunil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='medical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.medical'),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(blank=True, max_length=200, null=True)),
                ('degree', models.CharField(blank=True, max_length=200, null=True)),
                ('medical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.medical')),
            ],
        ),
    ]