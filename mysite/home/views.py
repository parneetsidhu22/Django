from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    # request -> POST,GET
    # location of file
    # templates/index.html
    return render(request, 'index.html', context={"name": "Parneet"})
