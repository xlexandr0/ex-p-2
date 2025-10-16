from rest_framework import serializers
from .models import Compania, Videojuego

class CompaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compania
        fields = ['id', 'nombre', 'pais']

class VideojuegoSerializer(serializers.ModelSerializer):
    # campo read-only anidado para mostrar info de la compañía
    compania_detalle = CompaniaSerializer(source='compania', read_only=True)
    # aceptamos escribir la compañía por id
    compania = serializers.PrimaryKeyRelatedField(queryset=Compania.objects.all())

    class Meta:
        model = Videojuego
        fields = ['id', 'titulo', 'genero', 'anio_lanzamiento', 'compania', 'compania_detalle']
