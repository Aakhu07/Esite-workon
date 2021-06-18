from django.urls import path
from .views import *

app_name = "ecomapp"
urlpatterns = [
    path("", HomeView.as_view(), name ="home"),
    path("all-products/", AllProductsView.as_view(), name ="allproducts"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name ="productdetail"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name ="addtocart"),
    path("my-cart/", MyCartView.as_view(), name ="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name ="managecart"),
]