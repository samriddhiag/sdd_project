from django.shortcuts import render
from .models import Request_student, Request_teacher, Request_hostel_owner
from .forms import StudentForm, HostelownerForm, TeacherForm
 
def Student_Form(request):
  if request.method == "POST":
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = StudentForm()
  return render(request, 'student_edit.html', {'form': form})

def Teacher_Form(request):
  if request.method == "POST":
    form = TeacherForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = TeacherForm()
  return render(request, 'student_edit.html', {'form': form})

def Hostelowner_Form(request):
  if request.method == "POST":
    form = HostelownerForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = HostelownerForm()
  return render(request, 'student_edit.html', {'form': form})