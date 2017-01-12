from django.contrib import admin
from . import models

class ItemAdmin(admin.ModelAdmin):
    
    search_fields = (
        'status',
        'name',
        'sku',
        'item_type',
        'category',
    )
    
    list_display = (
        'name',
        'sku',
        'date_created',
        'last_updated',
        'item_type',
        'get_category',
    )


admin.site.register(models.Items,ItemAdmin)
admin.site.register(models.ItemCategories)

# Register your models here.
