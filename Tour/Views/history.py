from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from . .models import *
from django.contrib import messages


def sowmya(request):
    if request.method == "POST":
        BookingId=request.POST.get('Booking Id')
        PackageName=request.POST.get('Package Name')
        PackageLocation=request.POST.get("PackageLocation")
        Package_type=request.POST.get("Package_type")
        Price=request.POST.get("Price")
        From=request.POST.get('From')
        To=request.POST.get('To')
        Comment=request.POST.get('Comment')
        data=Sowmya(BookingId=BookingId,PackageName=PackageName,PackageLocation=PackageLocation,Package_type=Package_type,Price=Price,From=From,To=To,Comment=Comment)
        data.save()
        messages.success(request,"New Tour package insert successfully")
        return render(request,'pages/admin_dashboard.html')
    else:
        return render(request,'pages/history.html')



def Rticket(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        Package_Name=request.POST.get("Package_Name")
        Package_Location=request.POST.get("Package_Location")
        comment=request.POST.get("comment")
        con=RaisedTicket(name=name,Package_Name=Package_Name,Package_Location=Package_Location,comment=comment)
        con.save()
        messages.success(request,"You raised a ticket")
        return render(request,'pages/user_dashboard.html')
    else:
        return render(request,'pages/user_dashboard.html')