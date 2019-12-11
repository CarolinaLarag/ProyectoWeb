from django import forms

from .models import Post, Proveedor

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'price']
        labels = {
            'title' : 'Nombre Producto',
            'text' : 'Descripcion',
            'image' : 'Imagen del Producto',
            'price' : 'Precio'
        }
        widgets = {
            'title' : forms.TextInput(attrs={ 'class': 'form-control'}),
            'text' : forms.TextInput(attrs={ 'class': 'form-control'}),
            'image' : forms.FileInput(attrs={ 'class': 'class="form-control-file'}),
            'price' : forms.NumberInput(attrs={ 'class': 'form-control'})
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['name', 'text', 'image']
        labels = {
            'name' : 'Nombre Proveedor',
            'text' : 'Descripcion',
            'image' : 'Imagen'
        }
        widgets = {
            'name' : forms.TextInput(attrs={ 'class': 'form-control'}),
            'text' : forms.TextInput(attrs={ 'class': 'form-control'}),
            'image' : forms.FileInput(attrs={ 'class': 'class="form-control-file'}),
        }