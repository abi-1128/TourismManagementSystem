from django.shortcuts import render,redirect,get_object_or_404
from . .models import *


def Package_details(request, id):
    data=get_object_or_404(Sowmya, id=id)
    return render(request,'pages/package_details.html',{'data':data})