from django.db import models

# Create your models here.

class Medical(models.Model):
    medical_name=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    mobile=models.IntegerField(unique=True)
    pin=models.IntegerField()
    gst_number=models.CharField(max_length=100, null=True)
    license_number=models.CharField(max_length=100, null=True)
    jurisdiction=models.CharField(max_length=100, null=True)
    status=models.IntegerField(default=1)
    date=models.DateField(auto_now_add=True,null=True)