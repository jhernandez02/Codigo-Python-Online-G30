from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from .models import Product

def home(request):
    return HttpResponse('👻 Bienvenido a mi aplicación con Django')

def get_date(request):
    now = datetime.now()
    html = f'<h1>Fecha y hora actuales: {now}</h1>'
    return HttpResponse(html)

def get_json(request):
    user = {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@example.com',
        'age': 30
    }
    return JsonResponse(user)

def get_html(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})