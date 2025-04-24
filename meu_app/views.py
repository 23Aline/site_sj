from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def vinicolas(request):
    return render(request, 'vinicolas.html')

def destaques(request):
    return render(request, 'destaques.html')

def clima(request):
    return render(request, 'clima.html')

def video(request):
    return render(request, 'video.html')