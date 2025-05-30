from django import forms
from .models import Usuario, Libro


#Formulario inicio de sesión
class LoginForm(forms.Form):
    correo = forms.EmailField(label="Correo Electrónico")


#Formulario registro de usuario
class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Correo'}),
        }


#Formulario de creacion de libro
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'valoracion']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título del libro'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Nombre del autor'}),
            'genero': forms.TextInput(attrs={'placeholder': 'Género'}),
            'valoracion': forms.NumberInput(attrs={'min': 1, 'max': 5, 'placeholder': 'Valor desde 1 hasta 5'}),
        }
    
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 2:
            raise forms.ValidationError("El título debe tener al menos 2 caracteres.")
        return titulo
    
    def clean_autor(self):
        autor = self.cleaned_data['autor']
        if len(autor) < 2:
            raise forms.ValidationError("El nombre del autor debe tener al menos 2 caracteres.")
        return autor
