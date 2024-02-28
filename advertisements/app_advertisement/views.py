from django.http import HttpResponse        # импорт объекта response для ответа сервера клиенту
from django.shortcuts import render, redirect
from django.urls  import reverse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):                         
    advertisements = Advertisement.objects.all()   #Вытаскиваем инфу из БД и вкладываем ее в переменную
    context = {'advertisements': advertisements}
    # return HttpResponse('Успешно')        # функция, возвращающая ответ "Успешно" на запрос пользователя
    return render(request, 'index.html', context)    # подключение к основному коду html-шаблона, который будет определять внешний вид главной страницы сайта 

def top_sellers(request):                      # функция render отправляет что-либо на сервер(сайт) 
    return render(request, 'top-sellers.html')# в кавычках прописывается название файла, который необходимо отправить на сервер(сайт)

def advertisement_post(request):                                  
    if request.method == 'POST':                                  # узнаем тип произошедщего запроса, и если это POST-запрос, делаем следующие действия
        form = AdvertisementForm(request.POST, request.FILES)     # создаем экземпляр класса, куда пойдут все данные и файлы от "анкеты" пользователя
        if form.is_valid():                                       # узнаем - валидны ли данные ползователя, если да, то выполняем следующие действия
            advertisement = Advertisement(**form.cleaned_data)    # создаем экземпляр класса объявлений и в качестве параметров закидываем данные от пользователя
            advertisement.user = request.user                     # добавляем имя пользователя и его id для отправления в базу данных
            advertisement.save()                                  # отправляем данные от пользователя в базу данных
            url = reversed('main_page')                           # генерируем маршрут к страницы при помощи ее имени
            return redirect(url)                                  # отправляем ответ пользователю
    else:
        form = AdvertisementForm()
    form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)