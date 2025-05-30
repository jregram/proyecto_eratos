# Proyecto Eratos

Aplicación web para gestionar una colección de libros, con login simulado y API REST.

## 🚀 Tecnologías

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- Bootstrap 5  
- django-widget-tweaks  

## 📥 Instalación

1. Clona el repositorio  
   ```bash
   git clone https://github.com/jregram/proyecto_eratos.git
   cd proyecto_eratos

2. Crea un entorno virtual e instálalo
   ```bash  
   python -m venv venv
   
   source venv/bin/activate   # macOS/Linux
   
   venv\Scripts\activate      # Windows
   
   pip install -r requirements.txt
   
3. Aplica migraciones
   ```bash
   python manage.py migrate

## ▶️ Ejecución en Local

1. python manage.py runserver
2. Abre tu navegador en http://127.0.0.1:8000/

## 📝 Uso (Web)

1. Login: ingresa tu correo (si no existe, te redirige a registro).
2. Registro: crea tu usuario con nombre y correo.
3. Lista de libros: consulta los libros existentes.
4. Crear libro: formulario con Título, Autor, Género y Valoración (1–5).
5. Detalle: ve la ficha completa y accede a Editar o Eliminar.
6. Editar / Eliminar: modifica datos o elimina el libro.
7. Logout: cierra sesión.

🌐 API REST

  ```bash
La API está expuesta bajo el prefijo /api/libros/

Método		Ruta			Descripción
GET		/api/libros/		Listar todos los libros
POST		/api/libros/		Crear un libro nuevo
GET		/api/libros/{id}/	Detalle de un libro
PUT		/api/libros/{id}/	Actualizar un libro
DELETE		/api/libros/{id}/	Eliminar un libro

Se puede probar desde curl o Postman


