from rest_framework import viewsets
from .models import Libro
from .serializers import LibroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    """
    Provee automáticamente:
      - list()   → GET    /api/libros/
      - retrieve() → GET   /api/libros/{pk}/
      - create()  → POST   /api/libros/
      - update()  → PUT    /api/libros/{pk}/
      - destroy() → DELETE /api/libros/{pk}/
    """