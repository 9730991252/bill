from django.db import models

# Create your models here.

class Medical(models.Model):
    medical_name=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    mobile=models.IntegerField(unique=True)
    pin=models.IntegerField()
    status=models.IntegerField(default=1)
    date=models.DateField(auto_now_add=True,null=True)