from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from products.models import Product
from clientes.models import Cliente
from .forms import OrderForm
from .forms import ReportFilterForm


def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}  # Asegúrate de que esto sea un diccionario, no un conjunto
    return render(request, 'orders/order_list.html', context)

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form':form})       

def report_view(request):
    orders = Order.objects.select_related('product').all()   
    return render(request, 'orders/report.html', {'orders': orders}) 

def report_view_form(request):
    form = ReportFilterForm(request.GET or None)  
    orders = Order.objects.select_related('product', 'cliente').all()  
    if form.is_valid():
        product = form.cleaned_data.get('product')
        cliente = form.cleaned_data.get('cliente')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        min_quantity = form.cleaned_data.get('min_quantity')
        max_quantity = form.cleaned_data.get('max_quentity')
        
        if product:
            orders = orders.filter(product = product)
        if cliente:
            orders = orders.filter(cliente = cliente)    
        if start_date:
            orders = orders.filter(created_at__gte = start_date) 
        if end_date:
            orders = orders.filter(created_at__gte = end_date) 
        if min_quantity is not None:
            orders = orders.filter(quantity__gte = min_quantity) #gte mayor
        if max_quantity is not None:
            orders = orders.filter(quantity__lte = max_quantity) #lte menor
    return render(request, 'orders/report_view.html', {'form':form, 'orders': orders})                    