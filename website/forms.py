from django import forms
from website.models import Product, Warehouse

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['address', 'postal', 'city', 'province']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'stock', 'desc', 'warehouseid']