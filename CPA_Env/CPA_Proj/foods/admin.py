from django.contrib import admin
from .models import Product, ProductDetails

#Adds FoodCategories class in admin db
admin.site.register(Product)
admin.site.register(ProductDetails)