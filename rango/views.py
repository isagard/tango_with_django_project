from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    string = "Rango says hey there partner!"
    link = "<a href='/rango/about/'>About</a>"
    response = string + link
    return HttpResponse(response)

def about(request):
    string = "Rango says here is the about page."
    link = "<a href='/rango/'>Index</a>"
    response = string + link
    return HttpResponse(response)



