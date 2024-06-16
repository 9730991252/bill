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
        l=[]
        medical_id = request.GET['medical_id']
        add_stock_id = request.GET['add_stock_id']
        item_id = request.GET['item_id']
        qty = request.GET['qty']
        sell_price_per_unit = request.GET['sell_price_per_unit']
        check_qty=int(qty)
        n = Add_stock.objects.get(id=add_stock_id)
        stock_qty = n.stock_qty
        stock_qty=int(stock_qty)
        stock_status = n.stock_status
        stock_status=int(stock_status)
        if check_qty <= stock_qty and stock_status == 1:
            Cart(
                medical_id=medical_id,
                add_stock_id=add_stock_id,
                item_id=item_id,
                qty=qty,
                sell_price_per_unit=sell_price_per_unit,

            ).save()
            s = Add_stock.objects.get(id=add_stock_id)
            s.stock_qty -= check_qty
            s.save()
        if 1 > stock_qty:
            k = Add_stock.objects.get(id=add_stock_id)
            k.stock_status = 0
            k.save()
        cart = Cart.objects.filter(medical_id=medical_id)
        qt=list(cart)
        ng=len(qt)
        if cart:
            for c in cart:
                a_id=c.add_stock_id
                a=Add_stock.objects.values().filter(id=a_id)
                a=list(a)
                l.extend(a)

        
        context={
                'cart':cart
        }
        t = render_to_string('ajax/cart.html', context)
    return JsonResponse({'data': t,'ng':ng,'add_stock':l})






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


def remove_cart(request):
    if request.method == 'GET':
        cart_id = request.GET['id']
        medical_id = request.GET['medical_id']
        k = Cart.objects.get(id=cart_id)
        k.qty
        s = Add_stock.objects.get(id=k.add_stock_id)
        s.stock_qty += k.qty
        s.save()
        Cart.objects.get(id=cart_id).delete()
        cart = Cart.objects.filter(medical_id=medical_id)
    context={
            'cart':cart
        }
    t = render_to_string('ajax/cart.html', context)
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

 

def sell_item_filter(request):
    if request.method == 'GET':
        words = request.GET['words']
        medical_id = request.GET['medical_id']
        if 1 < len(words):
            i=Add_stock.objects.filter(medical_id=medical_id,stock_status=1,item_name__icontains=words)[0:10]
        context={
                'i':i
                }
    t = render_to_string('ajax/sell_item_filter.html', context)
    return JsonResponse({'data': t})



def add_stock_item_filter(request):
    if request.method == 'GET':
        i={}
        words = request.GET['words']
        if 2 < len(words):
            i=Item.objects.filter(item_name__icontains=words).order_by('-item_name')
        context={
                'i':i
                }
    t = render_to_string('ajax/add_stock_item_filter.html', context)
    return JsonResponse({'data': t})

def doctor_filter(request):
    if request.method == 'GET':
        words = request.GET['words']
        degree = request.GET['degree']
        c_id = request.GET['c_id']
        d = ''
        if 2 < len(words) :
            d=Doctor.objects.filter(Q(doctor_name__icontains=words) )
        if 2 < len(degree) :
            d=Doctor.objects.filter(Q(degree__icontains=degree) )
        context={
                'd':d,
                'c_id':c_id
            }
        t = render_to_string('ajax/doctor_filter.html', context)
        return JsonResponse({'data': t})

def invice_filter(request):
    if request.method == "GET":
        p={}
        medical_id =request.GET['medical_id']
        k=Add_stock.objects.filter(medical_id=medical_id,stock_status=1).last()
        if k.party_id:
            p=Add_party.objects.get(id=k.party_id)
        a=Add_stock.objects.filter(stock_status=1,medical_id=medical_id).last()
        context={
                'a':a,
                'p':p
            }
        t = render_to_string('ajax/last_invice_filter.html', context)
        return JsonResponse({'data': t})

def add_party(request):
    if request.method == 'GET':
        medical_id = request.GET['medical_id']
        party_name = request.GET['party_name']
        party_address = request.GET['party_address']
        license_number = request.GET['license_number'].lower()
        gst_number = request.GET['gst_number'].lower()
        pl = ''
        pg = ''
        if license_number :
            pl = Add_party.objects.filter(license_number=license_number)
        if gst_number:
            pg = Add_party.objects.filter(gst_number=gst_number)
        if 0 == len(pl) and 0 == len(pg):
            Add_party(
                medical_id=medical_id,
                party_name=party_name,
                party_address=party_address,
                license_number=license_number,
                gst_number=gst_number
                ).save()
            party_id=Add_party.objects.filter(medical_id=medical_id).last()
            status = 1
        return JsonResponse({'status':status,'party_id':party_id.id})
    

def filter_party(request):
    if request.method == 'GET':
        party_name = request.GET['party_name']
        party_address = request.GET['party_address']
        license_number = request.GET['license_number'].lower()
        gst_number = request.GET['gst_number'].lower()
        if 2 < len(party_name) :
            p=Add_party.objects.filter(Q(party_name__icontains=party_name) )
        if 2 < len(party_address) :
            p=Add_party.objects.filter(Q(party_address__icontains=party_address) )
        if 2 < len(license_number) :
            p=Add_party.objects.filter(Q(license_number__icontains=license_number) )
        if 2 < len(gst_number) :
            p=Add_party.objects.filter(Q(gst_number__icontains=gst_number) )
        context={
                'p':p
            }
        t = render_to_string('ajax/party_filter.html', context)
        return JsonResponse({'data': t})