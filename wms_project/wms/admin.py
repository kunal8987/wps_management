from django.contrib import admin
from .models import SKU, MSKU

class SKUAdmin(admin.ModelAdmin):
    list_display = ('sku_code', 'name', 'description')  # Fields to display in the list view
    search_fields = ('sku_code', 'name')  # Fields to search in the admin interface
    list_filter = ('name',)  # Fields to filter by in the admin interface

class MSKUAdmin(admin.ModelAdmin):
    list_display = ('msku_code', 'name')  # Fields to display in the list view
    search_fields = ('msku_code', 'name')  # Fields to search in the admin interface
    list_filter = ('name',)  # Fields to filter by in the admin interface
    filter_horizontal = ('skus',)  # Allows for a better UI when selecting related SKUs

# Register the models with the admin site
admin.site.register(SKU, SKUAdmin)
admin.site.register(MSKU, MSKUAdmin)
