from rest_framework.routers import DefaultRouter
from .api import ProductoViewSet
from django.urls import path
from .views import register_user, user_login, user_logout

# Crear un enrutador
router = DefaultRouter()

router.register('api/productos', ProductoViewSet, basename='productos')

urlpatterns = [
    path('api/register/', register_user, name='register'),
    path('api/login/', user_login, name='login'),
    path('api/logout/', user_logout, name='logout'),
]

urlpatterns += router.urls