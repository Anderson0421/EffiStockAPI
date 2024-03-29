from rest_framework import serializers
from .models import Producto
from .models import CustomUser
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombre','marca','precio','fecha_ingreso','usuario','peso')
        read_only_fields = ('fecha_ingreso',)
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
