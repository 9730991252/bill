# Generated by Django 5.0.6 on 2024-06-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0032_alter_item_schedule_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_stock',
            name='schedule_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]