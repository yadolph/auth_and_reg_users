from django.shortcuts import render
from django.contrib.auth.models import User
from auth.forms import RegUser
from django.db import IntegrityError


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    result = ''
    form = RegUser()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')

        if password != password_check:
            return render(request, 'signup.html', {'result': 'Пароли не совпадают', 'form': form})

        try:
            new_user = User.objects.create_user(username, email=None, password=password)
        except IntegrityError:
            return render(request, 'signup.html', {'result': 'Такой пользователь уже существует', 'form': form})

        result = f'Пользователь {new_user.username} создан'

    return render(
        request,
        'signup.html',
        {'form': form, 'result': result}
    )
