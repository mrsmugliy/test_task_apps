from django.db import models


# Create your models here.
class Warehouse(models.Model):
    """
    Warehouse model attributes
    """
    name = models.CharField(max_length=64, verbose_name='Warehouse name')
    is_active = models.BooleanField(default=False)
    address1 = models.CharField(max_length=255, verbose_name='First address')
    address2 = models.CharField(max_length=255, verbose_name='Second address')
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    zip = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Date of change')


class WarehouseProduct(models.Model):
    """
    Warehouse product model attributes
    """
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    sku = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Date of change')
