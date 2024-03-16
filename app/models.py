from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
    Group,
        related_name='custom_users',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name=('groups')
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions')
    )
    
class Producto(models.Model):
    nombre = models.CharField(max_length=150,blank=False,null=False)
    marca = models.CharField(max_length=150,blank=False,null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
    fecha_ingreso = models.DateField(auto_now_add=True) 
    peso = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    