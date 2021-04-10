from django.shortcuts import render
from .models import Blog


def homepage(request):

    return render(request, 'index.html', context={"name": "Parneet"})
