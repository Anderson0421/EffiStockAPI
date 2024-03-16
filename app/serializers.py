from rest_framework import serializers
from .models import Producto
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombre','marca','precio','fecha_ingreso')
        read_only_fields = ('fecha_ingreso',)