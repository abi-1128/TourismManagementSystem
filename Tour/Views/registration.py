from django.shortcuts import render,redirect
from django.core.mail import send_mail
from . .models import Register
from django.contrib import messages



def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpw=request.POST.get('cpw')
        if password == cpw:
            data=Register(username=username,email=email,password=password)
            data.save()
            messages.success(request,"Registered succesfully")
        else:
            messages.error(request,"Password doesn't matched")
            return redirect('signup')
    else:
        return render(request,'pages/user_registration.html')
    
