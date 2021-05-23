from django.urls import path

from . import views

urlpatterns = [
    path("about",views.about, name="about"),
    path("home",views.home, name="home"),
    path("send_req",views.send_req, name="send_req"),
    path("register",views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout, name="logout")
    ]