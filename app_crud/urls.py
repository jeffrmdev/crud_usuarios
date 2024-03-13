from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('crear/', views.crear, name="crear")
]
