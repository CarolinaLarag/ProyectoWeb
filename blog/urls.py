from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('proveedores/<int:pk>/', views.proveedor_detail, name='proveedor_detail'),
    path('proveedores/new', views.proveedor_new, name='proveedor_new'),
    path('proveedores/<int:pk>/edit/', views.proveedor_edit, name='proveedor_edit'),
]
