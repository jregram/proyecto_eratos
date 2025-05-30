from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import LibroViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet, basename='libro')

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_usuario, name='usuario_registro'),
    path('', views.libros_list, name='libros_list'),
    path('libros/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/<int:id>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),

    #Rutas del API
    path('api/', include(router.urls)),
]
