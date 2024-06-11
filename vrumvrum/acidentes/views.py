from django.shortcuts import render
from django.http import HttpResponse

def acidentes(request):
    return render(request, 'tela_acidentes.html')
