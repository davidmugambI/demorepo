from django.db import models

# Create your models here.
choices = (
    ('Available', 'Item ready purchase'),
    ('Sold', 'Item sold'),
    ('Restocking', 'Restocking in few days')
)
class Desktop(models.Model):
    type = models.CharField(max_length=50,blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=30, choices=choices,
                              default='Available')
    issues = models.CharField(max_length=30, default='No issues')

class Laptop(models.Model):
    type = models.CharField(max_length=50,blank=False)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    status = models.CharField(max_length=30, choices=choices,
                              default='Available')
    issues = models.CharField(max_length=30, default='No issues')

class Mobile(models.Model):
    type = models.CharField(max_length=50,blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=30, choices=choices,
                              default='Available')
    issues = models.CharField(max_length=30, default='No issues')


