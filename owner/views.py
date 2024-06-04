from django.shortcuts import render, redirect
from sunil .models import *
from owner .models import *
from django.template.loader import render_to_string
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages 
from django.db.models import Sum
# Create your views here.

def owner_dashboard(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        o = Order_Master.objects.all()
        context={
            'o':o
        }
        return render(request,'owner/owner_dashboard.html',context)
    else:
        return redirect('/')
    
     
def item(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
        if 'Add_Item'in request.POST:
            item_name = request.POST.get('item_name')
            image = request.FILES.get("image")
            Item(
                medical_id=m.id,
                item_name = item_name,
                image = image
            ).save()
            return redirect('/owner/item/')
        context={
                'i':Item.objects.filter(medical_id=m.id)[0:1],
                'm':m
        }
        return render(request,'owner/item.html', context)
    else:
        return redirect('/')
    




def stock_item_filter(request):
    if request.method == 'GET':
        words = request.GET['words']
        medical_id = request.GET['medical_id']
        if 2 < len(words):

            i=Item.objects.filter(medical_id=medical_id,item_name__icontains=words)
    context={
            'i':i
        }
    t = render_to_string('ajax/stock_item_filter.html', context)
    return JsonResponse({'data': t})





@csrf_exempt
def add_stock(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
        if 'Add_Stock_Item'in request.POST:
            item_id = request.POST.get('item_id')
            print(item_id)
            price = request.POST.get('price')
            add_qty = request.POST.get('add_qty')
            invice_number = request.POST.get('invice_number')
            expiry_date = request.POST.get('expiry_date')
            Add_stock(
                medical_id=m.id,
                item_id = item_id,
                price = price,
                add_qty = add_qty,
                stock_qty = add_qty,
                invice_number = invice_number,
                expiry_date = expiry_date,
            ).save()
            return redirect('/owner/add_stock/')
        context={
            'i':Item.objects.filter(medical_id=m.id)[0:1],
            'm':m
        }
        return render(request,'owner/add_stock.html', context)
    else:
        return redirect('/')




@csrf_exempt
def sell_item(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        c = ''
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
        if 'Remove_cart_item' in request.POST:
            cart_id = request.POST.get('cart_id')
            k = Cart.objects.get(id=cart_id)
            k.qty
            s = Add_stock.objects.get(id=k.add_stock_id)
            s.stock_qty += k.qty
            s.save()
            Cart.objects.get(id=cart_id).delete()
            return redirect('/owner/sell_item/')
        if 'Add_Customer' in request.POST:
            customer_name = request.POST.get('customer_name')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            if Customer.objects.filter(mobile=mobile).exists():
                messages.warning(request,"Owner Mobile Allready Exists")
            else:
                Customer(
                    customer_name=customer_name,
                    mobile=mobile,
                    address=address,
                ).save()
                c = Customer.objects.get(mobile=mobile)
        if 'Select_Customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            c = Customer.objects.get(id=customer_id)
        if 'Complete_Order' in request.POST:
            customer_id = request.POST.get('customer_id')
            t = Cart.objects.filter(medical_id=m.id).aggregate(Sum("total_price"))
            t = t['total_price__sum']
            f=Order_Master.objects.filter(medical_id=m.id).count()
            f+=1
            Order_Master(
                medical_id=m.id,
                customer_id=customer_id,
                payment_status=1,
                total_amount=t,
                order_filter=f,
            ).save()
            cart = Cart.objects.filter(medical_id=m.id)
            if cart:
                for cart in cart:
                    prc = cart.price
                    prc = str(prc)
                    nqty = cart.qty
                    nqty = str(nqty)
                    Order_detail(
                        medical_id=cart.medical_id,
                        customer_id=customer_id,
                        item_id=cart.item_id,
                        invice_number=cart.add_stock.invice_number,
                        expiry_date=cart.add_stock.expiry_date,
                        item_name=cart.item.item_name,
                        qty=nqty,
                        price=prc,
                        total_price=cart.total_price,
                        order_filter=f,
                        ).save()
            Cart.objects.filter(medical_id=m.id).delete()
            return redirect('/')
        context={
            'i':Add_stock.objects.filter(medical_id=m.id,stock_status=1)[0:5],
            'm':m,
            'cart':Cart.objects.filter(medical_id=m.id),
            'c':c,
            'filter_c':Customer.objects.all()
            }
        return render(request,'owner/sell_item.html', context)
    else:
        return redirect('/')



def complate_view_order(request, id):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
        t = Order_detail.objects.filter(medical_id=m.id,order_filter=id).aggregate(Sum("total_price"))
        t = t['total_price__sum']
        item = Order_detail.objects.filter(medical_id=m.id,order_filter=id)
        if item:
            for i in item:
                bill_number=i.order_filter
                date=i.ordered_date
                customer_id=i.customer_id
        if customer_id == None:
            customer_name = ''
            mobile = ''
        else:
            c = Customer.objects.get(id=customer_id)
            customer_name = c.customer_name
            mobile = c.mobile
            print('hi')
        context={
                'o':Order_detail.objects.filter(medical_id=m.id,order_filter=id),
                'm':m,
                'bill_number':bill_number,
                'date':date,
                't':t,
                'customer_name':customer_name,
                'mobile':mobile,
        }
        return render(request, 'owner/complate_view_order.html', context)
    else:
        return redirect('/')
    




def complate_bill(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
        o = Order_Master.objects.filter(medical_id=m.id)
        context={
            'o':o
        }
        return render(request, 'owner/complate_bill.html', context)
    else:
        return redirect('/')
    
