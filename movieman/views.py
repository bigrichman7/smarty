from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'movieman/index.html')

def game(request):
    return render(request, 'movieman/game.html')
