from django import from forms 
from .models import Product

class ProductForm(forms.ModelForn):
    class meta:
        model = Product
        fields = ['name', 'description', 'precio', 'stock']