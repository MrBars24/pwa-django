from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout", views.logout, name="logout"),
    path("offline", views.offline, name="offline"),
    path("push/<int:userid>", views.push, name="push")
]
