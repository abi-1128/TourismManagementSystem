from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from . .models import *
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        request.session['username']=username
        if Register.objects.filter(username=username).exists():
            obj1=Register.objects.get(username=username)
            request.session['email']=obj1.email
            obj2=Register.objects.filter(username=username).values()
            if obj1.password == password:
                data1=Sowmya.objects.all().values()
                data2=MyBookings.objects.all().values()
                return render(request,'pages/user_dashboard.html',{'obj2':obj2,'data1':data1,'data2':data2})
            else:
                messages.error(request,"you entered invalid password")
                return redirect('login')
        else:
            messages.error(request,"No such user Exists")
            return redirect('login')
    else:
        return render(request,'pages/login.html')    



@login_required
def book_now(request,package_id):
    if request.method == 'POST':
        # Retrieve the UserRegister instance
        package = Sowmya.objects.get(id=package_id)
        PackageName = package.PackageName
        user_register = get_object_or_404(Register, username=request.session.get("username"),email=request.session.get("email"))
        created = MyBookings.objects.get_or_create(username=user_register,email=user_register,PackageName=package)
        package=MyBookings.objects.filter(PackageName=package).values()
        email=user_register.email
        # if created:
        #     # Send confirmation email
        #     subject = 'Booking Confirmation'
        #     message = f'You tour was booked. Your booked tour is {package_name}'
        #     from_email = 'your@example.com'  # Update with your email address
        #     recipient_list = [email]
        #     send_mail(subject, message, from_email, recipient_list)
            
        #     messages.info(request, 'Booking successful. Confirmation email sent.')
        # else:
        #     messages.warning(request, 'Booking already exists.')
        messages.success(request,"Ticket booking Successfully")
        return render(request,'pages/user_dashboard.html')
    else:
        # Handle case where request method is not POST
        return redirect('login')
