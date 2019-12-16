from django.urls import path, re_path, include
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login', views.login, name='index'),
    path('logout', views.logout, name='logout'),
    path('register', views.register),
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/delete/<int:id>', views.post_delete, name='post_delete'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('proveedores/<int:pk>/', views.proveedor_detail, name='proveedor_detail'),
    path('proveedores/new', views.proveedor_new, name='proveedor_new'),
    path('proveedores/<int:pk>/edit/', views.proveedor_edit, name='proveedor_edit'),
    path('proveedores/delete/<int:id>', views.proveedor_delete, name='proveedor_delete'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='blog/password_reset.html', email_template_name="blog/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), name = 'password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html') , name = 'password_reset_complete'),

]
