from django.shortcuts import render

def index(request):
    return render(request, 'website/welcomepage.html')

def HomePage(request):
    return render(request, 'website/index.html')