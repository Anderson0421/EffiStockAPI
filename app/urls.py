from rest_framework import routers
from .api import CategoriaViewSet,ProductoViewSet

router = routers.DefaultRouter()

router.register('api/categorias',CategoriaViewSet,'categorias')
router.register('api/productos',ProductoViewSet,'productos')

urlpatterns = router.urls