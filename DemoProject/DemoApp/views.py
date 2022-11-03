from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse("<center><h2> Hello User<br/>Welcome to Django World</h2><center>");
