from django.shortcuts import render
from django.contrib.auth.models import User
from auth.forms import RegUser, LoginUser
from django.db import IntegrityError
from django.contrib.auth import authenticate, logout, login


def home(request):
    username = request.user
    logged_in = True
    if request.user.is_anonymous:
        print('ok')
        username = 'Гость'
        logged_in = False

    return render(
        request,
        'home.html',
        {'username': username, 'logged_in': logged_in}
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


def login_user(request):
    result = ''
    form = LoginUser()

    if request.user.is_authenticated:
        print(request.user)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            result = 'Вы успешно вошли в систему'
        else:
            result = 'Ошибка. Проверьте введенные данные'

    return render(
        request,
        'login.html',
        {'form': form, 'result': result}
    )

def logout_user(request):
    logout(request)

    return render(
        request,
        'logout.html',
    )
