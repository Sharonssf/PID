from django.urls import path
from . import views

urlpatterns = [
    path('acidentes/', views.acidentes, name = "acidentes")
]