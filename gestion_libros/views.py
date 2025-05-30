from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegistroUsuarioForm, LibroForm
from .models import Usuario, Libro
from django.urls import reverse
from django.contrib import messages

#Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            try:
                usuario = Usuario.objects.get(correo=correo)
                request.session['usuario_id'] = usuario.id
                messages.success(request, "Has iniciado sesión correctamente. ¡Bienvenido de nuevo!")
                return redirect('libros_list')
            except Usuario.DoesNotExist:
                messages.error(request, "Correo no registrado. Debes crear una cuenta primero.")
                return redirect(f"{reverse('usuario_registro')}?correo={correo}")

    else:
        form = LoginForm(initial={'correo': request.GET.get('correo', '')})

    return render(request, 'gestion_libros/login.html', {'form': form})


#Logout
def logout_view(request):
    # Limpia la sesión del usuario
    request.session.flush()

    return redirect('login')


#Registro de Usuario
def registro_usuario(request):
    initial = {}
    if 'correo' in request.GET:
        initial['correo'] = request.GET['correo']

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, "Usuario registrado. ¡Bienvenido!")
            request.session['usuario_id'] = usuario.id
            return redirect('libros_list')
        
    else:
        form = RegistroUsuarioForm(initial=initial)
    
    return render(request, 'gestion_libros/registro.html', {'form': form})


#Listar los libros
def libros_list(request):
    #Proteger la vista de usuarios no logueados
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    libros = Libro.objects.all()

    return render(request, 'gestion_libros/libros_list.html', {'libros': libros})


#Detalles del libro
def detalle_libro(request, id):
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    libro = get_object_or_404(Libro, id=id)
    
    return render(request, 'gestion_libros/detalle_libro.html', {'libro': libro})


#Creacion de libros
def crear_libro(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado correctamente.")
            return redirect('libros_list')
    else:
        form = LibroForm()

    return render(request, 'gestion_libros/crear_libro.html', {'form': form})


#Editar informacion de libro
def editar_libro(request, id):
    if 'usuario_id' not in request.session:
        return redirect('login')

    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado correctamente.")
            return redirect('detalle_libro', id=libro.id)
    else:
        form = LibroForm(instance=libro)

    return render(request, 'gestion_libros/editar_libro.html', {'form': form, 'libro': libro})


#Eliminación de libro
def eliminar_libro(request, id):
    if 'usuario_id' not in request.session:
        return redirect('login')

    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.delete()
        messages.success(request, "Libro eliminado correctamente.")
        return redirect('libros_list')

    return render(request, 'gestion_libros/eliminar_libro.html', {'libro': libro})