from django.db import models


import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        
        return False

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    Category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=50, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def get_products_by_id(ids):
        return Products.objects.filter(id__in =ids)
    
    def get_all_products():
        return Products.objects.all()
    
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(Category=category_id)
        else:
            return Products.get_all_products()

class Order(models.Model):
    Product= models.ForeignKey(Products, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address= models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date= models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    def get_orders_by_customer(customer_id):
        return Order.objects.filter(Customer=customer_id).order_by('-date')

