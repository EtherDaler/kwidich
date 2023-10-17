from . import models
from .decorators import unauthenticated, authenticated, admin
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


@unauthenticated
def main(request):
    return render(request, "mainApp/main.html")


@authenticated
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            login_object = User.objects.get(phone=username)
        except:
            login_object = None
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Неверный номер телефона или пароль!')

    context = {}
    return render(request, "mainApp/login.html", context)


@unauthenticated
def logout_page(request):
    logout(request)
    return redirect('main')


@authenticated
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.info(request, 'Пароли не совпадают!')
            return redirect("registration")
        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user is None:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, "Такой пользователь уже существует!")

    context = {}
    return render(request, "mainApp/register.html", context)
