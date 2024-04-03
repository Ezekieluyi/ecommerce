from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from decouple import config
# Create your views here.

def home(request):
    email = EmailMessage("Visitor Alert", "You have a new visitor",config("email_host"), ["godstimeizedowa@gmail.com"])
    email.send()
    return render (request, "app/index.html")

@login_required
def profile(request):
    return render (request, "app/profile.html")

def error404(request, exception):
    return render ( request, "app/error404.html", status = 404)

def error500(request):
    return render (request, "app/error500.html", status= 500)