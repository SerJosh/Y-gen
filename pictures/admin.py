from django.contrib import admin
from .models import Product, Category, Review
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

@admin.register(models.Review)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'name')
    search_fields = ('name', 'content')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
