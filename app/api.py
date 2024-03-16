from rest_framework import viewsets,permissions
from .serializers import ProductoSerializer
from .models import Producto




class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    
