from django import forms
from .models import Request_student, Request_hostel_owner,Request_teacher

 
class StudentForm(forms.ModelForm):
  class Meta:
    model = Request_student
    fields = ["roll_num", "email_std","message","document"]
    labels = {'roll_num': "Roll number", "email_std": "Email Address",'message': "Enter Message",'document':"Upload a doc"}

class HostelownerForm(forms.ModelForm):
  class Meta:
    model = Request_hostel_owner
    fields = ["hostel_id", "owner_name","message","document"]
    labels = {'hostel_id': "Unique Hostel ID", "owner_name": "Owner Name",'message': "Enter Message",'document':"Upload a doc"}

class TeacherForm(forms.ModelForm):
  class Meta:
    model = Request_teacher
    fields = ["teacher_id", "teacher_subject","message","document"]
    labels = {'teacher_id': "Unique Teacher ID", "teacher_subject": "Subject",'message': "Enter Message",'document':"Upload a doc"}