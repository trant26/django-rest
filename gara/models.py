from django.core import validators
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from .validators import validate_category, validate_number, validate_phone, validate_name


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdraw')
)

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=256)

    def __str__(self):
        return self.manufacturer_name 

class Vehicle(models.Model): 
    vehicle_name = models.CharField(max_length=256)  
    model = models.CharField(max_length=256)
    seria_number = models.CharField(max_length=256)
    year = models.DateField()
    model = models.CharField(max_length=256)
    cost = models.FloatField(validators=[validate_number])
    amount_sale = models.FloatField(validators=[validate_number])
    manufacturer = models.ForeignKey(Manufacturer, related_name='Manufacturer', null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return self.vehicle_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=256, validators=[validate_name])
    customer_adddress = models.CharField(max_length=256)
    customer_phone = models.CharField(max_length=11)
    def __str__(self):
        return self.customer_name

class Salesman(models.Model):
    salesman_name = models.CharField(max_length=256, validators=[validate_name])
    salesman_adddress = models.CharField(max_length=256)
    salesman_phone = models.CharField(max_length=256, validators=[validate_phone])
    def __str__(self): 
        return self.salesman_name     



class Option(models.Model):
    part_name = models.CharField(max_length=256)
    quanity = models.FloatField()
    amount_sale = models.FloatField()
    def __str__(self):
        return self.part_name

class Invoice(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer, related_name='Customer', null=True, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='Vehicle', null=True, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Salesman, related_name='Salesman', null=True, on_delete=models.CASCADE)
    is_tradein = models.BooleanField()
    price_sold = models.FloatField()
    part_id = models.ManyToManyField(Option)
    

class Car(models.Model): 
    created = models.DateTimeField(auto_now_add=True)
    vehicle_name = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    seria_number = models.CharField(max_length=256)
    year = models.DateTimeField()
    model = models.CharField(max_length=256, validators=[validate_category])
    cost = models.FloatField(max_length=100)
    amount_sale = models.FloatField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='car', on_delete=models.CASCADE)
    highlighted = models.TextField()
    class Meta:
        ordering = ('created',)


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __string__(self):
        return self.email