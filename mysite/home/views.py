from django.shortcuts import render


def homepage(request):
    print(request.POST.get('username'))
    return render(request, 'index.html', context={"name": "Parneet"})
