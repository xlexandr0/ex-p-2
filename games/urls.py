from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CompaniaViewSet, VideojuegoViewSet

router = DefaultRouter()
router.register(r'companias', CompaniaViewSet, basename='companias')
router.register(r'videojuegos', VideojuegoViewSet, basename='videojuegos')

urlpatterns = [
    path('', include(router.urls)),
]
