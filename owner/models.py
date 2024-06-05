from django.db import models
from sunil.models import *
from PIL import Image
# Create your models here.

class Item(models.Model):
    medical = models.ForeignKey(Medical,on_delete=models.PROTECT,null=True)
    item_name=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True,null=True)


INSTOCK_OUTSTOCK_CHOICE=(
    ('1','in stock'),
    ('0','out of stock'),
    ('2','cancel'),
)
class Add_stock(models.Model):
    medical = models.ForeignKey(Medical,on_delete=models.PROTECT,null=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT,null=True)
    price = models.IntegerField()
    add_qty = models.IntegerField()
    stock_qty = models.IntegerField()
    invice_number = models.IntegerField(null=True)
    expiry_date = models.DateField(max_length=100, null=True)
    stock_status = models.IntegerField(choices=INSTOCK_OUTSTOCK_CHOICE,default=1)
    added_date = models.DateField(auto_now_add=True)

class Customer(models.Model):
    customer_name = models.CharField(max_length=200,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    


STATUS_CHOICES = (
  ('1','Paid'),
  ('0','UnPaid'),
)

    
class Cart(models.Model):
    medical = models.ForeignKey(Medical,on_delete=models.PROTECT,null=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT,null=True)
    add_stock = models.ForeignKey(Add_stock,on_delete=models.PROTECT,null=True)
    qty = models.IntegerField()
    price = models.FloatField(default=0,null=True)
    total_price=models.FloatField(default=0,null=True)
    def save(self,*args,**kwargs):
        price=eval(self.price)
        qty=eval(self.qty)
        #print(type(qty))
        self.total_price=price*qty
        super(Cart,self).save()

class Order_Master(models.Model):
    medical = models.ForeignKey(Medical,on_delete=models.PROTECT,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,null=True)
    payment_status = models.CharField(choices=STATUS_CHOICES,default='0',max_length=50)
    total_amount=models.FloatField(default=0,null=True)
    order_filter=models.IntegerField(default=True)
    date=models.DateField(auto_now_add=True,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)



class Order_detail(models.Model):
    medical = models.ForeignKey(Medical,on_delete=models.PROTECT,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,null=True)
    invice_number = models.IntegerField(null=True)
    expiry_date = models.CharField(max_length=100, null=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT,null=True)
    item_name = models.CharField(max_length=200)
    qty = models.IntegerField()
    price = models.FloatField(default=0,null=True)
    total_price=models.FloatField(default=0,null=True)
    order_filter=models.IntegerField(default=True)
    date=models.DateField(auto_now_add=True,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    def save(self,*args,**kwargs):
        price=eval(self.price)
        qty=eval(self.qty)
        #print(type(qty))
        self.total_price=price*qty
        super(Order_detail,self).save()