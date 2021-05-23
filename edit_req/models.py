from django.db import models

# Create your models here.
class Request_student(models.Model):
    roll_num = models.IntegerField()
    email_std = models.CharField(max_length=100)
    message = models.TextField()
    document = models.ImageField(upload_to='pics')

class Request_hostel_owner(models.Model):
    hostel_id = models.IntegerField()
    owner_name = models.CharField(max_length=100)
    message = models.TextField()
    document = models.ImageField(upload_to='pics')

class Request_teacher(models.Model):
    teacher_id = models.IntegerField()
    teacher_subject = models.CharField(max_length=100)
    message = models.TextField()
    document = models.ImageField(upload_to='pics')