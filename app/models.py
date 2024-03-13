from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=150,blank=False,null=False)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150,blank=False,null=False)
    marca = models.CharField(max_length=150,blank=False,null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
    fecha_ingreso = models.DateField(auto_now_add=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre