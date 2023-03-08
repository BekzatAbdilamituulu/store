from django.contrib import admin
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'price', 'quantity', 'images', 'categories')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(OrderItems)
admin.site.register(Orders)
admin.site.register(Users)
admin.site.register(Categories, CategoriesAdmin)
