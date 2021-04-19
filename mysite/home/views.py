from django.shortcuts import render
from .models import Blog


def homepage(request):
    if request.method == "POST":
        msg = request.POST.get("msg_box")

        if msg != '':
            blog = Blog(msg=msg)
            blog.save()
    data = Blog.objects.all()

    return render(request, 'index.html', context={"msgs": data})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request,'register.html')