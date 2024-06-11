from django.shortcuts import render
from django.http import HttpResponse

def adicionar_semaforo(request):
    return render(request, 'tela_add_semaforo.html')

def controle_semaforo(request):
    return render(request, 'tela_controle_semaforo.html')