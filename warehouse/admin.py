from django.contrib import admin

from .models import Warehouse, WarehouseProduct


class WarehouseProductInline(admin.TabularInline):
    """
    View a list of products for a warehouse
    """
    model = WarehouseProduct
    readonly_fields = ('sku', 'name', 'created_at', 'modified_at')
    can_delete = False
    max_num = 0


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    """
    Admin panel for the Warehouse model
    """
    list_display = ('__str__', 'name', 'is_active', 'created_at', 'modified_at')
    inlines = [WarehouseProductInline]


@admin.register(WarehouseProduct)
class WarehouseProductAdmin(admin.ModelAdmin):
    """
    Admin panel for the WarehouseProduct model
    """
    list_display = ('sku', 'name', 'created_at', 'modified_at', 'warehouse')
