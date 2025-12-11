from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . .models import *

@ login_required
def adminlogin(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None :
            data1=Register.objects.all().values()
            data2=Sowmya.objects.all().values()
            data3=Enquiry.objects.all().values()
            data4=RaisedTicket.objects.all().values()
            context ={
                'data1':data1,
                'data2':data2,
                'data3':data3,
                'data4':data4,
            }
            return render(request,'pages/admin_dashboard.html',context)
        else:
            adminlogin(request,user)
            messages.error(request,"No such user Exists")
            return redirect('adminlogin')
    else:
        return render(request,'pages/adminlogin.html')



