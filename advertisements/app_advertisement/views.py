from django.http import HttpResponse        # импорт объекта response для ответа сервера клиенту
from django.shortcuts import render
from .models import Advertisement

def index(request):                         
    advertisements = Advertisement.objects.all()   #Вытаскиваем инфу из БД и вкладываем ее в переменную
    context = {'advertisements': advertisements}
    # return HttpResponse('Успешно')        # функция, возвращающая ответ "Успешно" на запрос пользователя
    return render(request, 'index.html', context)    # подключение к основному коду html-шаблона, который будет определять внешний вид главной страницы сайта 

def top_sellers(request):                      # функция render отправляет что-либо на сервер(сайт) 
    return render(request, 'top-sellers.html')# в кавычках прописывается название файла, который необходимо отправить на сервер(сайт)

