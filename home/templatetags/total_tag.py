from django import template
from owner.models import *
from django.db.models import Avg, Sum, Min, Max
from math import *

register = template.Library()

@register.simple_tag
def total_price_owner(id):
    p=Cart.objects.filter(medical_id=id)
    n=0
    if p:
        for p in p:
            a=p.total_price
            n += a
        return n
