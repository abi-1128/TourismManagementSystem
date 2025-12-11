
from django.urls import path
from .Views.homepage import home
from .Views.user_enquiry import Enquiry
from .Views.registration import signup
from .Views.login import login,book_now
from .Views.admin_dashboard import *
from .Views.history import sowmya,Rticket 
from .Views.adminlogin import adminlogin
from .Views.package_details import Package_details
urlpatterns=[
     path('',home, name='homepage'),
     path('Enquiry',Enquiry,name='Enquiry'),
     path('signup',signup,name='signup'),
     path('login/',login,name='login'),
     path('Admin_dashboard',admin_dashboard,name='admin_dashboard'),
     path('Sowmya',sowmya,name='Sowmya'),
     path('adminlogin',adminlogin,name='adminlogin'),
     path('PackageDetails/<int:id>/',Package_details,name='Package_details'),
     path('RaisedTicket',Rticket,name='Rticket'),
     path('Bookings/<package_id>/',book_now,name='book_now'),
]