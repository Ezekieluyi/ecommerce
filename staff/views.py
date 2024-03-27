from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from product.models import Product


# Create your views here.
@login_required
def admin(request):
    user = request.user
    if not user.is_staff:
        return redirect(reverse("app:home"))
    all_product = Product.objects.all().order_by("-created_at")
    context = {"products": all_product}
    return render(request, "staff/admin.html", context)

@login_required
def edit(request, id):
    user = request.user
    if not user.is_staff:
        return redirect(reverse("app:home"))
    item = Product.objects.filter(id=id).first()
    if not item :
        return redirect(reverse("staff:home"))
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        item.name = name
        item.description = description
        item.quantity = quantity
        item.price = price
        if image:
            item.image = image
        item.save()
        messages.success(request, "item has been updated successfully")
        return redirect(reverse("staff:home"))
    context = {"product":item}
    return render(request, "staff/edit.html", context)

@login_required
def delete(request, id):
    user = request.user
    if not user.is_staff:
        return redirect(reverse("app:home"))
    item = Product.objects.filter(id=id).first()
    if not item :
        return redirect(reverse("staff:home"))
    item.delete()
    messages.success(request, "item has been deleted")
    return redirect(reverse("staff:home"))

@login_required
def create (request):
    user = request.user
    if not user.is_staff:
        return redirect(reverse("app:home"))
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        new_product = Product.objects.create(
            name = name,
            description = description,
            price = price,
            image = image,
            quantity = quantity
        )
        new_product.save()
        messages.success(request, "product created successfully")
        return redirect(reverse("staff:home"))
    return render(request, "staff/create.html")