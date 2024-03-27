from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path ("product", views.product, name = "product"),
    path ('details/<str:id>', views.details, name = "details"),
    path ("buy/<str:id>", views.buy, name= "buy"),
]