from django.core import validators
from django.db import models
from pygments.lexers import get_all_lexers

LEXERS = [item for item in get_all_lexers() if item[1]]

class Manufacturer(models.Model):
    # manufacturerId = models.AutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=256)

    def __str__(self):
        return self.manufacturer_name

class Vehicle(models.Model):
    # id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    seria_number = models.CharField(max_length=256)
    year = models.DateField()
    model = models.CharField(max_length=256)
    cost = models.FloatField()
    amount_sale = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer, related_name='Manufacturer', null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.vehicle_name


class Customer(models.Model):
    # id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=256)
    customer_adddress = models.CharField(max_length=256)
    customer_phone = models.CharField(max_length=11)
    def __str__(self):
        return self.customer_name

class Salesman(models.Model):
    # id = models.AutoField(primary_key=True)
    salesman_name = models.CharField(max_length=256)
    salesman_adddress = models.CharField(max_length=256)
    salesman_phone = models.CharField(max_length=256)
    def __str__(self):
        return self.salesman_name



class Option(models.Model):
    # id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=256)
    quanity = models.FloatField()
    amount_sale = models.FloatField()
    def __str__(self):
        return self.part_name

class Invoice(models.Model):
    # id = models.AutoField(primary_key=True)
    date = models.DateField()
    customer = models.ForeignKey(Customer, related_name='Customer', null=True, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='Vehicle', null=True, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Salesman, related_name='Salesman', null=True, on_delete=models.CASCADE)
    is_tradein = models.BooleanField()
    price_sold = models.FloatField()
    # def vehicle(self):
    #     return 



class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    vehicle_name = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    seria_number = models.CharField(max_length=256)
    # year = models.DateTimeField()
    model = models.CharField(max_length=256)
    cost = models.FloatField(max_length=100)
    amount_sale = models.FloatField(max_length=100)
    class Meta:
        ordering = ('created',)