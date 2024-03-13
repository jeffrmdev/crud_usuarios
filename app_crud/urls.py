from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('crear/', views.crear, name="crear"),
    path('editar_usuario/<int:persona_id>', views.guardar_edicion, name="editar_usuario"),
    path('editar/<int:persona_id>', views.editar, name="editar"),
    path('eliminar/<int:persona_id>', views.eliminar, name="eliminar"),
]
