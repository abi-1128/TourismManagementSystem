from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

def sowmi(request):
    template = loader.get_template('pages/home.html')
    return HttpResponse(template.render())