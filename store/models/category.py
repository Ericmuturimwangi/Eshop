from django.db import models


import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)

    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name