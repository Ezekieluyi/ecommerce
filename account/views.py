from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    user = request.user
    if user.is_authenticated:
        return redirect (reverse("app:home"))
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("con")
        if not username or not email or not password or not confirm_password:
            messages.error(request, "incomplete details")
            return render (request, "account/signup.html")
        if len(password) <8:
            messages.error(request, "password is too short")
            return render (request, "account/signup.html")
        if password != confirm_password :
            messages.error(request, "password does not match")
            return render (request, "account/signup.html")
        if User.objects.filter(username = username). exists():
            messages.error(request, "username already exist")
            return render (request, "account/signup.html")
        if User.objects.filter(email = email). exists():
            messages.error(request, "email already in use")
            return render (request, "account/signup.html")
        profile = User.objects.create(username = username, email = email)
        profile.set_password(password)
        profile.save()
        messages.success(request, "account created successfully")
        return redirect (reverse("account:login"))
        
    return render (request, "account/signup.html")

def login(request):
    user = request.user
    if user.is_authenticated:
        return redirect (reverse("app:home"))
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
            messages.error(request, "incomplete details")
            return render (request, "account/login.html")
        profile = auth.authenticate(username=username, password=password)
        if not profile:
            messages.error(request, "incorrect credentials")
            return render (request, "account/login.html")
        auth.login(request, profile)
        messages.success(request, "login successful")
        return redirect (reverse("app:home"))
    return render (request, "account/login.html")

def logout(request):
    auth.logout(request)
    return redirect (reverse("account:login"))