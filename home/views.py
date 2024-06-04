from django.shortcuts import render ,redirect
from django.contrib import messages 
from sunil.models import *
from owner.models import *
# Create your views here.
def index(request):
    #Order_detail.objects.all().delete()
    #Order_Master.objects.all().delete()
    #Add_stock.objects.all().delete()
    #Item.objects.all().delete()
    if request.session.has_key('owner_mobile'):
        return redirect('/owner/owner_dashboard/')
    if 'Login' in request.POST:
        num=request.POST.get('mobile')
        pin=request.POST.get('pin')
        sunil_login={'mobile':'9730991252','pin':'7878'}
        if sunil_login["mobile"]==num and sunil_login["pin"]==pin:
            request.session['sunil_mobile'] = request.POST.get('mobile')
            return redirect('/sunil/sunil_dashboard/')
        m= Medical.objects.filter(mobile=num,pin=pin,status=1)
        if m:
            request.session['owner_mobile'] = request.POST.get('mobile')
            return redirect('/owner/owner_dashboard/')
        messages.warning(request,"please insert correct information or call more suport 9730991252")        
    return render(request, 'home/index.html')

def contact_us(request):
    return render(request, 'home/contact_us.html')

def woner_logout(request):
    del  request.session['owner_mobile']
    return redirect('/')

