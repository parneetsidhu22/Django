from django.shortcuts import render
from .models import Blog


def homepage(request):
    if request.method == "POST":
        msg=request.POST.get("msg_box")
        if msg!='':
            blog=Blog(msg=msg)
            blog.save()

    return render(request, 'index.html', context={"name": "Parneet"})
