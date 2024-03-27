from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.

@login_required
def product(request):
    all_products = Product.objects.all().order_by('-created_at')
    context = {"products": all_products}
    return render (request, "product/product.html", context)

@login_required
def details(request, id):
    details = Product.objects.filter(id=id).first()
    if not details :
        return redirect(reverse("product:product"))
    context = {"product":details}
    return render(request, "product/details.html", context)

@login_required
def buy(request, id):
    buy = Product.objects.filter(id=id).first()
    if not buy :
        return redirect(reverse("product:details"))
    context = {"product":buy}
    return render(request, "product/buy.html", context)