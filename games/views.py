from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Compania, Videojuego
from .serializers import CompaniaSerializer, VideojuegoSerializer

class CompaniaViewSet(viewsets.ModelViewSet):
    queryset = Compania.objects.all()
    serializer_class = CompaniaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['nombre', 'pais']

class VideojuegoViewSet(viewsets.ModelViewSet):
    queryset = Videojuego.objects.select_related('compania').all()
    serializer_class = VideojuegoSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # habilitamos ?search= para titulo y genero
    search_fields = ['titulo', 'genero']
    # también permitir filtrado por compania id y año
    filterset_fields = ['compania', 'anio_lanzamiento']
