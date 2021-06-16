from django.urls import path
from .views import *

app_name = "ecomapp"
urlpatterns = [
    path("", HomeView.as_view(), name ="home"),
    path("all-products/", AllProductsView.as_view(), name ="allproducts"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name ="productdetail"),

]