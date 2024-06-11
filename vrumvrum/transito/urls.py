from django.urls import path
from . import views

urlpatterns = [
    path('adicionarsemaforo/', views.adicionar_semaforo, name='adicionarsemaforo'),
    path('controlesemaforo/', views.controle_semaforo, name='controlesemaforo'),
]
