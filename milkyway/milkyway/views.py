# milkyway/views.py
from django.shortcuts import render


def index(request):
    render(request, 'templates/index.html', {'foo': 'bar'})
