from django import forms

from .models import Post, Proveedor

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'price']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['name', 'text', 'image']