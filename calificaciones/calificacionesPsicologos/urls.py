from django.urls import path 
from . import views

urlpatterns = [
    path('create/<int:id_usuario>', views.psicologo_view_noid, name='psicologo_view_noid'),
    path('<int:id>', views.psicologo_view, name='psicologo_view'),
    path("calificacion/<int:id_psicologo>", views.calificacion_view, name='calificacion_view'), 
    path("delete/<int:id_usuario>/<int:id>", views.delete_psicologo_view, name="delete_psicologo_view")
]

