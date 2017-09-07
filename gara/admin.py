from django.contrib import admin

from .models import Vehicle, Manufacturer, Customer, Salesman, Option, Invoice

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_name')
    search_fields = ['vehicle_name']

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer_name')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name')

class SalesmanAdmin(admin.ModelAdmin):
    list_display = ('id', 'salesman_name')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'salesman', 'vehicle')

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Salesman, SalesmanAdmin)
admin.site.register(Option)
admin.site.register(Invoice, InvoiceAdmin)