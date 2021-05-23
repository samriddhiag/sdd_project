from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def home(request):
    
    dests= Destination.objects.all()

    return render(request, 'homepage.html',{'dests': dests})
