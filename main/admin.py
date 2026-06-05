from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'category', 'created_at', 'updated_at']
    list_editable = ['price', 'is_active']
    prepopulated_fields = {'slug':('name', )}