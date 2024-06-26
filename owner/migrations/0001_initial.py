# Generated by Django 5.0.6 on 2024-06-01 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sunil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images')),
                ('status', models.IntegerField(default=1)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('medical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.medical')),
            ],
        ),
    ]
