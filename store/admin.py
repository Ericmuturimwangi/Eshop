from django.contrib import admin
from .models import Order, Customer, Products, Category
# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)

