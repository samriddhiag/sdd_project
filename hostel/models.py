from django.db import models

# Create your models here.

class Hostels(models.Model):
    img = models.ImageField(upload_to='pics')
    hostel_id = models.IntegerField()
    hostel_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=25)
    hostel_address = models.TextField()