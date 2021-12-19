from django.contrib import admin
from django.urls import path, include
from .views import product_list, product_detail, manufacturer_list, manufacturer_detail # ProductDetailView, ProductsListView

urlpatterns = [
    path('products/', product_list, name="product-list"),
    path('product/<int:pk>/', product_detail, name="product-detail"),
    path('manufacturers/', manufacturer_list, name="manufacturer-list"),
    path('manufacturer/<int:pk>/', manufacturer_detail, name="manufacturer-detail"),
    # path('list/', ProductsListView.as_view(), name="products-list"),
    # path('detail/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
]
