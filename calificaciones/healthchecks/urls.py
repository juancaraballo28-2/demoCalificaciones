from django.urls import path 
from . import views

urlpatterns = [
    path('<int:id>', views.get_healthcheck_view, name='get_healthcheck_view'),
    path('create/<int:id_usuario>', views.post_healthcheck_view, name="post_healthcheck_view"),
]