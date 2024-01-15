from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpResponse) -> HttpResponse:
    return render(request, 'index.html')

def about(request: HttpResponse) -> HttpResponse:
    return render(request, 'about.html')

def contact(request: HttpResponse) -> HttpResponse:
    return render(request, 'contact.html')