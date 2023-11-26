from django.db import models

import datetime

# Create your models here.
class Category (models.Model):
    name= models.CharField(max_length=250)

    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField()
    password= models.CharField(max_length=100)

    def register(self):
        self.save()

    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    def isExists(self):
        if Customer.objects.filter(email= self.email):
            return True
        
        return False
    
class Products(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def get_products_by_id(ids):
        return Products.objects.filter(id_in=ids)
    
    def get_all_products():
        return Products.objects.all()
    
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address=models.CharField(max_length=30, default='', blank=True)
    phone=models.CharField(max_length=40, default='', blank=True)
    date= models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def placeOrder(self):
        self.save()


    def get_orders_by_customer(customer_id):
        return Order.objects.filter(Customer-customer_id).order_by('-date')

