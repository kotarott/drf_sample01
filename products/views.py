from django.shortcuts import render
from .models import Product, Manufacturer

from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    data = {
        "products": list(products.values("pk", "name", "price"))
    }
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse(
            {
                "error": {
                    "code": 404,
                    "message": "product not found!"
                }
            },
            status=404
        )
    return response

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {
        "Manufacturers": list(manufacturers.values("pk", "name", "location"))
    }
    response = JsonResponse(data)
    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {
            "product": {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": list(manufacturer_products.values())
            }
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse(
            {
                "error": {
                    "code": 404,
                    "message": "Manufacturer not found!"
                }
            },
            status=404
        )
    return response

# below codes: using django template 
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_details.html"

# class ProductsListView(ListView):
#     model = Product
#     template_name = "products/products_list.html"