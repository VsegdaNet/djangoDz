from django.contrib import admin
from TaskDz02.models import Product, Order
# Register your models here.



@admin.register(Product)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'quantity', 'data']
    prepopulated_fields = {'slug': ('product_name',)}


@admin.register(Order)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['data_order']