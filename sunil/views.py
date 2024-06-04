from django.shortcuts import render,redirect
from sunil.models import *
from django.contrib import messages 
# Create your views here.

def sunil_dashboard(request):
    if request.session.has_key('sunil_mobile'):
        sunil_mobile = request.session['sunil_mobile']
        return render(request,'sunil/sunil_dashboard.html')
    else:
        return redirect('/')
    

def add_medical(request):
    m=Medical.objects.all()
    if request.session.has_key('sunil_mobile'):
        sunil_mobile = request.session['sunil_mobile']
        print(sunil_mobile)
        if 'Add_Medical' in request.POST:
            medical_name = request.POST.get('medical_name')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if Medical.objects.filter(mobile=mobile).exists():
                messages.warning(request,"Owner Mobile Allready Exists")
            else:
                Medical(
                    medical_name = medical_name,
                    address = address,
                    mobile = mobile,
                    pin = pin
                    ).save()
                return redirect('add_medical')
        context={
            'm':m
        }
        return render(request,'sunil/add_medical.html', context)
    else:
        return redirect('/')
    