from django.contrib import admin
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['title', 'description']
    list_display = ['__unicode__', 'price', 'active', 'updated_at', 'created_at']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated_at', 'created_at']
    prepopulated_fields = {'slug': ('title', )}

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)