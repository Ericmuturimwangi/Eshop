from django.db import models
from store.models.products import Products
from store.models.customer import Customer
import datetime

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
