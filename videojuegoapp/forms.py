from django import forms
from django.contrib.auth.forms import UserCreationForm

from videojuegoapp.models import *
COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

class UserForm (UserCreationForm):
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username', 'password1', 'password2']


class CreateFormGenero (forms.Form):
    nombre = forms.CharField(max_length=40)


class UpdateFormGenero (forms.Form):
    nombre = forms.CharField(max_length=40)
    fecha_creacion = forms.DateField()


class FormPlataforma (forms.Form):
    nombre = forms.CharField(max_length=40)
    fecha_lanzamiento = forms.DateField()


class FormDesarrollador (forms.Form):
    nombre = forms.CharField(max_length=100)
    fundacion = forms.DateField()
    web_url = forms.CharField(max_length=255)


class FormAutor (forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_nacimiento = forms.DateField()
    foto_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class FormPost (forms.Form):
    titulo = forms.CharField(max_length=255)
    contenido = forms.CharField(widget=forms.Textarea)
    imagen_url = forms.CharField(max_length=255)
    autor = forms.ChoiceField(choices=[])
    categoria = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(FormPost, self).__init__(*args, **kwargs)
        self.fields['autor'].choices = [(x.pk, x.user.username) for x in Autor.objects.all()]
        self.fields['categoria'].choices = [(x.pk, x.nombre) for x in Categoria.objects.all().order_by("nombre")]

class FormVideojuego (forms.Form):
    nombre = forms.CharField(max_length=255)
    genero = forms.ChoiceField(choices=[])
    desarrollador = forms.ChoiceField(choices=[])
    fecha_lanzamiento = forms.DateField()
    plataformas = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)
   
    def __init__(self, *args, **kwargs):
        super(FormVideojuego, self).__init__(*args, **kwargs)
        self.fields['genero'].choices = [(x.pk, x.nombre) for x in Genero.objects.all().order_by("nombre")]
        self.fields['desarrollador'].choices = [(x.pk, x.nombre) for x in Desarrollador.objects.all().order_by("nombre")]
        self.fields['plataformas'].choices = [(x.pk, x.nombre) for x in Plataforma.objects.all().order_by("nombre")]

class FormCategoria (forms.Form):
    nombre = forms.CharField(max_length=40)

class FormEditProfile (forms.Form):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email' ]

class FormEditPassword (forms.Form):
    password1 = forms.CharField(label='Contraseña Nueva', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña Nueva', widget=forms.PasswordInput(attrs={'class': 'form-control'}))