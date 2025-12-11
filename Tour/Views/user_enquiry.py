from django.shortcuts import render,redirect
from django.contrib import messages
from . .models import Enquiry




def Enquiry(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        Mobile_Number=request.POST.get("Mobile_Number")
        subject=request.POST.get("subject")
        description=request.POST.get("description")
        con= Enquiry(name=name,email=email,Mobile_Number=Mobile_Number,subject=subject,description=description)
        con.save()
        messages.success(request,"Enquiry send successfully")
        return redirect('Enquiry')
    else:
        return render(request,'pages/enquiry.html')