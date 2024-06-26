from django.shortcuts import render, redirect
from sunil .models import *
from owner .models import *
from django.template.loader import render_to_string
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages 
from django.db.models import Sum
from datetime import date
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
    
     
def item_name(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
        context={
                'i':Item.objects.filter(medical_id=m.id)[0:1],
                'm':m
        }
        return render(request,'owner/item.html', context)
    else:
        return redirect('/')
    





@csrf_exempt
def add_stock(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        item = ''
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
            today = date.today()
            today_list = Add_stock.objects.filter(medical_id=m.id,added_date__gte=today,added_date__lte=today)
        if 'Select_Item' in request.POST:
            item_id = request.POST.get('item_id')
            item = Item.objects.get(id=item_id)
        if 'Add_Stock_Delete'in request.POST:
            stock_delete_id = request.POST.get('stock_delete_id')
            Add_stock.objects.get(id=stock_delete_id).delete()
            return redirect('/owner/add_stock/')
        if 'Add_Stock_Item'in request.POST:
            medical_id = request.POST.get('medical_id')
            party_id = request.POST.get('party_id')
            item_id = request.POST.get('item_id')
            item_name = request.POST.get('item_name').lower()
            company_name = request.POST.get('company_name')
            item_type = request.POST.get('item_type')
            schedule_type = request.POST.get('schedule_type')
            purchase_price = request.POST.get('purchase_price')
            gst = request.POST.get('gst')
            qty = request.POST.get('qty')
            qty_stripe = request.POST.get('qty_stripe')
            temp_qty = request.POST.get('temp_qty')
            total_purchase_price= request.POST.get('total_purchase_price')
            disc_qty= request.POST.get('disc_qty')
            disc_price= request.POST.get('disc_qty')
            disc_qty_stripe= request.POST.get('disc_qty_stripe')
            disc_temp_qty= request.POST.get('disc_temp_qty')
            total_qty = int(temp_qty) + int(disc_temp_qty)
            invice_number = request.POST.get('invice_number').lower() 
            party_name = request.POST.get('parti_name') 
            expiry_date = request.POST.get('expiry_date') 
            n=expiry_date
            d='01'
            expiry_date=f"{n}-{d}"
            if expiry_date == '-01':
                expiry_date = None
            batch_number = request.POST.get('batch_number') 
            sell_price_per_unit = request.POST.get('sell_price_per_unit') 
            if Item.objects.filter(item_name=item_name).exists():
                Add_stock(
                    medical_id=medical_id,
                    party_id=party_id,
                    item_name=item_name,
                    item_id=item_id,
                    company_name=company_name,
                    item_type=item_type,
                    schedule_type=schedule_type,
                    purchase_price=purchase_price,
                    gst=gst,
                    qty=qty,
                    qty_stripe=qty_stripe,
                    temp_qty=temp_qty,
                    total_purchase_price=total_purchase_price,
                    disc_qty=disc_qty,
                    disc_price=disc_price,
                    disc_qty_stripe=disc_qty_stripe,
                    disc_temp_qty=disc_temp_qty,
                    total_qty=total_qty,
                    stock_qty=total_qty,
                    invice_number=invice_number,
                    party_name=party_name,
                    expiry_date=expiry_date,
                    batch_number=batch_number,
                    sell_price_per_unit=sell_price_per_unit,
                    ).save()
                return redirect('/owner/add_stock/')
            else:
                Item(
                    medical_id=medical_id,
                    item_name=item_name,
                    item_type=item_type,
                    schedule_type=schedule_type,
                    company_name=company_name,
                ).save()
                new_i=Item.objects.filter(medical_id=medical_id).last()
                Add_stock(
                    medical_id=medical_id,
                    party_id=party_id,
                    item_name=item_name,
                    item_id=new_i.id,
                    company_name=company_name,
                    item_type=item_type,
                    schedule_type=schedule_type,
                    purchase_price=purchase_price,
                    gst=gst,
                    qty=qty,
                    qty_stripe=qty_stripe,
                    temp_qty=temp_qty,
                    total_purchase_price=total_purchase_price,
                    disc_qty=disc_qty,
                    disc_price=disc_price,
                    disc_qty_stripe=disc_qty_stripe,
                    disc_temp_qty=disc_temp_qty,
                    total_qty=total_qty,
                    stock_qty=total_qty,
                    invice_number=invice_number,
                    party_name=party_name,
                    expiry_date=expiry_date,
                    batch_number=batch_number,
                    sell_price_per_unit=sell_price_per_unit,
                    ).save()
       
            return redirect('/owner/add_stock/')
        context={
            #'i':Item.objects.filter(medical_id=m.id)[0:10],
            'm':m,
            'item':item,
            'today_list':today_list,
            'p':Add_party.objects.all()[0:2]
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
        doctor = ''
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
        if 'Add_Customer' in request.POST:
            customer_name = request.POST.get('customer_name')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            if Customer.objects.filter(mobile=mobile).exists():
                messages.warning(request,"Owner Mobile Allready Exists")
            else:
                Customer(
                    medical_id=m.id,
                    customer_name=customer_name,
                    mobile=mobile,
                    address=address,
                ).save()
                c = Customer.objects.get(mobile=mobile)
        if 'Add_Doctor' in request.POST:
            customer_id = request.POST.get('customer_id')
            doctor_name = request.POST.get('doctor_name').lower()
            degree = request.POST.get('degree').lower()
            if Doctor.objects.filter(doctor_name=doctor_name,degree=degree).exists():
                doctor = Doctor.objects.get(doctor_name=doctor_name,degree=degree)
                c = Customer.objects.get(id=customer_id)
            else:
                Doctor(
                   medical_id=m.id,
                   doctor_name=doctor_name,
                   degree=degree 
                ).save()
                doctor = Doctor.objects.get(doctor_name=doctor_name,degree=degree)
                c = Customer.objects.get(id=customer_id)
        if 'Select_Customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            c = Customer.objects.get(id=customer_id)
        if 'Select_Doctor' in request.POST:
            doctor_id = request.POST.get('doctor_id')
            c_id = request.POST.get('c_id')
            doctor = Doctor.objects.get(id=doctor_id)
            c = Customer.objects.get(id=c_id)
        if 'Complete_Order' in request.POST:
            customer_id = request.POST.get('customer_id')
            doctor_id = request.POST.get('doctor_id')
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
                    prc = cart.sell_price_per_unit
                    prc = str(prc)
                    nqty = cart.qty
                    nqty = str(nqty)
                    Order_detail(
                        medical_id=cart.medical_id,
                        doctor_id=doctor_id,
                        customer_id=customer_id,
                        item_id=cart.item_id,
                        add_stock_id=cart.add_stock_id,
                        qty=nqty,
                        sell_price_per_unit=prc,
                        order_filter=f,
                        ).save()
            Cart.objects.filter(medical_id=m.id).delete()
            return redirect(f'/owner/complate_view_order/{f}')
        context={
            'i':Add_stock.objects.filter(medical_id=m.id,stock_status=1)[0:25],
            'm':m,
            'cart':Cart.objects.filter(medical_id=m.id),
            'c':c,
            'filter_c':Customer.objects.all(),
            'd':Doctor.objects.all(),
            'doctor':doctor
            }
        return render(request,'owner/sell_item.html', context)
    else:
        return redirect('/')



def complate_view_order(request, id):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        customer_id=0
        c = ''
        d = ''
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
                doctor_id=i.doctor_id
        if customer_id == None:
            customer_name = ''
            mobile = ''
        else:
            c = Customer.objects.get(id=customer_id)
            d = Doctor.objects.get(id=doctor_id)
        context={
                'o':Order_detail.objects.filter(medical_id=m.id,order_filter=id),
                'm':m,
                'bill_number':bill_number,
                'date':date,
                't':t,
                'c':c,
                'd':d
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
    
def profile(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        m=Medical.objects.filter(mobile=owner_mobile).first()
        if m:
            m=Medical.objects.get(mobile=owner_mobile)
        if 'Edit_Profile' in request.POST:
            medical_id = request.POST.get('medical_id')
            medical_name = request.POST.get('medical_name')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            gst_number = request.POST.get('gst_number')
            license_number = request.POST.get('license_number')
            jurisdiction = request.POST.get('jurisdiction')
            Medical(
                medical_name=medical_name,
                address=address,
                mobile=mobile,
                pin=pin,
                gst_number=gst_number,
                license_number=license_number,
                jurisdiction=jurisdiction,
                id=medical_id,
                ).save()
            return redirect('/owner/profile/')
        context={
            'm':m
        }
        
        return render(request, 'owner/profile.html', context)
    else:
        return redirect('/')