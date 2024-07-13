from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def startingpage(request):
    return HttpResponse("Hello World, I'm Shafin. Hottest/smartest human alive <3")
