from django.db import models
from products.models import Product
from clientes.models import Cliente

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True) #antes de migrar (blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return f"Order{self.id} - {self.product.name} - {self.cliente.nombre}"