from django.urls import path

from . import views

urlpatterns = [
    path("Student_Form", views.Student_Form, name='Student_Form'),
    path("Teacher_Form", views.Teacher_Form, name='Teacher_Form'),
    path("Hostelowner_Form", views.Hostelowner_Form, name='Hostelowner_Form')
    ]
    