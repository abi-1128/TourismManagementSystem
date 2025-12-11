from django.contrib import admin
from Tarak.models import *


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display=("username","email","password",)
    
admin.site.register(Register,MemberAdmin)

class TourAdmin(admin.ModelAdmin):
    list_display=("BookingId","PackageName","PackageLocation","Package_type","Price","From","To","Comment",)
    
admin.site.register(Sowmya,TourAdmin)


class EnquiryAdmin(admin.ModelAdmin):
    list_display=("name","email","Mobile_Number","subject","description",)
    
admin.site.register(Enquiry,EnquiryAdmin)


class RaisedTicketAdmin(admin.ModelAdmin):
    list_display=("name","Package_Name","Package_Location","comment",)

admin.site.register(RaisedTicket,RaisedTicketAdmin)




class BookingsAdmin(admin.ModelAdmin):
    list_display=("username","email","PackageName",)

admin.site.register(MyBookings,BookingsAdmin)