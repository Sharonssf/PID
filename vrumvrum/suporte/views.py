from django.shortcuts import render
from django.http import HttpResponse

def suporte(request):
    return render(request, 'tela_suporte.html')

def sobre(request):
    return render(request, 'tela_sobre_nos.html')