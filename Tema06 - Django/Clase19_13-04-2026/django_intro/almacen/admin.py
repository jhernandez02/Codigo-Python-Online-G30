from django.contrib import admin
from .models import Category, Product

class CategoyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'is_active', 'stock', 'category')
    search_fields = ('name',)


admin.site.register(Category, CategoyAdmin)
admin.site.register(Product, ProductAdmin)
