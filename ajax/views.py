from django.shortcuts import render, redirect
from sunil .models import *
from owner .models import *
from django.template.loader import render_to_string
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages 
from django.db.models import Sum
from django.db.models import Q
# Create your views here.


def add_to_cart(request):
    if request.method == 'GET':
        qty = request.GET['qty']
        price = request.GET['price']
        medical_id = request.GET['medical_id']
        add_stock_id = request.GET['add_stock_id']
        item_id = request.GET['item_id']
        check_qty=int(qty)
        n = Add_stock.objects.get(id=add_stock_id)
        stock_qty = n.stock_qty
        stock_qty=int(stock_qty)
        stock_status = n.stock_status
        stock_status=int(stock_status)
        add_qty = n.add_qty
        add_qty=int(add_qty)
        if check_qty <= stock_qty and stock_status == 1:
            Cart(
                qty=qty,
                price=price,
                medical_id=medical_id,
                add_stock_id=add_stock_id,
                item_id=item_id,
            ).save()
            s = Add_stock.objects.get(id=add_stock_id)
            s.stock_qty -= check_qty
            s.save()
        if 1 > stock_qty:
            print('hi')
            k = Add_stock.objects.get(id=add_stock_id)
            k.stock_status = 0
            k.save()
        cart = Cart.objects.filter(medical_id=medical_id)
        qt=list(cart)
        ng=len(qt)
        context={
                'cart':cart
        }
        t = render_to_string('ajax/cart.html', context)
    return JsonResponse({'data': t,'ng':ng})






def new_item_filter(request):
    if request.method == 'GET':
        words = request.GET['words']
        medical_id = request.GET['medical_id']
        if 2 < len(words):

            i=Item.objects.filter(medical_id=medical_id,item_name__icontains=words)
    context={
            'i':i
        }
    t = render_to_string('ajax/new_item_filter.html', context)
    return JsonResponse({'data': t})






def customer_filter(request):
    if request.method == 'GET':
        customer_mobile = request.GET['customer_mobile']
        customer_name = request.GET['customer_name']
        customer_address = request.GET['customer_address']
        if 4 < len(customer_name) :
            c=Customer.objects.filter(Q(customer_name__icontains=customer_name) )

        if 4 < len(customer_mobile):
            c=Customer.objects.filter(Q(mobile__icontains=customer_mobile) )

        if 4 < len(customer_address):
            c=Customer.objects.filter(Q(address__icontains=customer_address) )

        context={
                'c':c
            }
        t = render_to_string('ajax/customer_filter.html', context)
        return JsonResponse({'data': t})
