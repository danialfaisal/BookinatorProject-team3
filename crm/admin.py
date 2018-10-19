from django.contrib import admin

from .models import Customer, Service, Product


class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'organization', 'phone_number' )
    list_filter = ( 'cust_name', 'organization')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class ServiceList(admin.ModelAdmin):
    list_display = ( 'category', 'name', 'author')
    list_filter = ( 'category', 'name')
    search_fields = ('category', )
    ordering = ['category']

class ProductList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'product', 'pickup_time')
    list_filter = ( 'cust_name', 'pickup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)