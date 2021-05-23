from django.shortcuts import render
from .models import Hostels

# Create your views here.
def hostel(request):
    
    hosts= Hostels.objects.all()

    return render(request, 'hostel.html',{'hosts': hosts})