from django import forms 
from .models import Order, Product, Cliente

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'cliente', 'quantity']
        
class ReportFilterForm(forms.Form):
    product = forms.ModelChoiceField(queryset = Product.objects.all(), required=False, label="Producto")    
    cliente = forms.ModelChoiceField(queryset = Cliente.objects.all(), required=False, label="Cliente")  
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}), label="Fecha inicio")
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}), label="Fecha de fin")
    min_quantity = forms.IntegerField(required=False, label="Cantidad minima")  
    max_quantity = forms.IntegerField(required=False, label="Cantidad Maxima")