from rest_framework import serializers
from .models import Libro

#Traductor entre instancias de modelos (objetos Python) y representaciones JSON que envía y recibe la API.

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'genero', 'valoracion']