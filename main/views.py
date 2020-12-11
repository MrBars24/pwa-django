from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from webpush import send_user_notification

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        users = User.objects.all().exclude(is_superuser=True) if request.user.is_superuser else None
        return render(request, "index.html", {"users": users})     
    return render(request, "guest.html", {})
def logout(request):
    django_logout(request)
    return redirect("home")
def offline(request):
    return render(request, "offline.html", {})
def push(request, userid):
    user = User.objects.get(pk=userid)
    payload = {
        "head": "PWA Django",
        "body": "Welcome to PWA Django, " + user.first_name
    }
    send_user_notification(user=user, payload=payload, ttl=0)
    return redirect("home")