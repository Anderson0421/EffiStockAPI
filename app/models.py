from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=150,blank=False,null=False)
    marca = models.CharField(max_length=150,blank=False,null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
    fecha_ingreso = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.nombre