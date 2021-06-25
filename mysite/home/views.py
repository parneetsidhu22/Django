from django.shortcuts import render, redirect
from .models import Blog

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="/login")
def homepage(request):
    if request.method == "POST":
        msg = request.POST.get("msg_box")

        if msg != '':
            blog = Blog(msg=msg)
            blog.save()

    data = Blog.objects.all()

    return render(request, 'index.html', context={"msgs": data})


def mylogout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('homepage')


def mylogin(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("homepage")
        else:
            messages.error(request, "Invalid Credentials!")
    return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        errors = False

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.",
                           extra_tags="username_error")
            errors = True

        user = User.objects.filter(username=username)
        if user != None:
            errors = True

            messages.error(request, "Username already exists.",
                           extra_tags="username_error")

        if password != cpassword:
            messages.error(request, "Password does not match.",
                           extra_tags="password_error")
            errors = True

        if not errors:

            user = User(username=username, email=email)
            user.first_name = fname
            user.last_name = lname
            user.set_password(password)
            user.save()

            user2 = authenticate(request, username=username, password=password)

            if user2 != None:
                login(request, user2)
            else:
                pass
                # error messages

            messages.success(request, 'Welcome...')
            return redirect('homepage')
    return render(request, 'register.html')
