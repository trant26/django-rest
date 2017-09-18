from django.contrib import admin
from gara.models import Vehicle
from .form import SignUpForm
from .models import SignUp

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = 'Mark selected stories as published'

from .models import Vehicle, Manufacturer, Customer, Salesman, Option, Invoice

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_name', 'status')
    search_fields = ['vehicle_name']
    actions = [make_published]
 
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer_name')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name')

class SalesmanAdmin(admin.ModelAdmin):
    list_display = ('id', 'salesman_name')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'salesman', 'vehicle')


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__string__", "timestamp", "update"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Salesman, SalesmanAdmin)
admin.site.register(Option)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(SignUp, SignUpAdmin)
