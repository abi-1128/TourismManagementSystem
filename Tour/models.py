from django.db import models

 # Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=10)

def __str__(self):
    return f"{self.username}"

class Sowmya(models.Model):
    BookingId=models.IntegerField(null=True)
    PackageName=models.CharField(max_length=255)
    PackageLocation=models.CharField(max_length=255)
    TYPE_CHOICES=[('AllServices','AllServices'),('FoodService','FoodService'),('TravelService','TravelService'),('Accomdation','Accomdation'),]
    Package_type=models.CharField(max_length=20,choices=TYPE_CHOICES)
    Price=models.IntegerField(null=True)
    From=models.DateField(null=True)
    To=models.DateField(null=True)
    Comment=models.CharField(max_length=255)


def __str__(self):
    return f"{self.name}"


class Enquiry(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(null=True)
    Mobile_Number=models.IntegerField(null=True)
    subject=models.CharField(max_length=20)
    description=models.CharField(max_length=255)

def __str__(self):
    return f"{self.username}"


class RaisedTicket(models.Model):
    name=models.CharField(max_length=255)
    Package_Name=models.CharField(max_length=255)
    Package_Location=models.CharField(max_length=255)
    comment=models.CharField(max_length=255)

def __str__(self):
    return f"{self.username}"


class MyBookings(models.Model):
    username = models.ForeignKey(Register, on_delete=models.CASCADE)
    email = models.EmailField()
    PackageName=models.ForeignKey(Sowmya, on_delete=models.CASCADE)
    
def __str__(self):
    return f"{self.username}"