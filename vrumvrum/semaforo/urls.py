from django.urls import path
from . import views

urlpatterns = [
    path('semaforo/', views.semaforo, name='semaforo'),
]
