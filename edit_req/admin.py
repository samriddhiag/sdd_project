from django.contrib import admin
from .models import Request_student, Request_hostel_owner,Request_teacher

# Register your models here.

admin.site.register(Request_student)
admin.site.register(Request_hostel_owner)
admin.site.register(Request_teacher)