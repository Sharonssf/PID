from django.urls import path
from . import views

urlpatterns = [
    path('suporte/', views.suporte, name = "suporte"),
    path('sobre/', views.sobre, name = "sobre_nos")
]