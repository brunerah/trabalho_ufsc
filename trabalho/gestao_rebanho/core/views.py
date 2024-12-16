from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def base(request):
    return render(request, 'base.html')

