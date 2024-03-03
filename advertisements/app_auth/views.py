from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm
# Create your views here.

@login_required(login_ur = reverse_lazy('profile'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    if request.method == 'GET':                         # если пользователь нажал на вход, то
        if request.user.is_authenticated:               # если пользователь уже зарегестрирован
            return redirect(reverse('profile'))         # направляем его в личный кабинет
        else:                                           # если нет
            return render(request,'app_auth/login.html')  # отправляем регестрироваться
    username = request.POST['username']                 # узнаю имя пользователя 
    password = request.POST['password']                 # узнаю пароль
    user = authenticate(request, username=username, password=password) # проверка на совпадение логина и пароля
    if user is not None:                                # если пользователь есть в базе
        login(request, user)                            # логиним его
        return redirect(reverse('profile'))             # и перекидываем в личный кабинет
    return render(request,'app_auth/login.html',{'error': 'Пользователь не найден'}) # иначе выдаем ошибку 

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register_view(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user=user)
            return redirect(reverse('profile'))
    else:
        form = ExtendedUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'app_auth/register.html', context)