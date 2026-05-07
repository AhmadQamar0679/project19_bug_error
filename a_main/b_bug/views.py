from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    messages.debug(request,'This is dbug message.')
    messages.info(request,'This is an info message')
    return render (request,'home.html')