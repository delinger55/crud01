from django.shortcuts import render, get_object_or_404, redirect
#from .models import Order
from .models import Cliente
from .forms import ClienteForm


# Create your views here.
def cliente_list(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}  # Asegúrate de que esto sea un diccionario, no un conjunto
    return render(request, 'clientes/cliente_list.html', context)

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form':form}) 


#leer detalle
def cliente_detail(request, id):
    cliente = get_object_or_404(Cliente, pk=id)   
    return render(request, 'clientes/cliente_detail.html', {'cliente':cliente})

def cliente_update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)   
    return render(request, 'clientes/cliente_form.html', {'form':form})   

def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})       
