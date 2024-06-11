from django.shortcuts import render
from django.http import HttpResponse

def semaforo(request):
    return render(request, 'tela_controle_transito.html')