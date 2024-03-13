from rest_framework import serializers
from .models import Producto,Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nombre',)
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombre','marca','precio','fecha_ingreso','categoria')
        read_only_fields = ('fecha_ingreso',)