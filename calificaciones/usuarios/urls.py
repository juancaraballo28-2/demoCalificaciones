from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_usuario_view, name='post_usuario_view'),
    path('<int:id>', views.usuario_view, name='usuario_view'),
]