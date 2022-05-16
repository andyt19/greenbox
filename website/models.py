from django.db import models

class Warehouse(models.Model):
    address = models.CharField(max_length=100)
    postal = models.CharField(max_length=7)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'warehouses'

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    desc = models.CharField(max_length=500)
    warehouseid = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
