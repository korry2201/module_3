from django.http import HttpResponse        # импорт объекта response для ответа сервера клиенту
from django.shortcuts import render, redirect
from django.urls  import reverse, reverse_lazy
from django.core import validators
from .models import Advertisement
from .forms import AdvertisementForm, New_model_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

def index(request):                         
    title = request.GET.get('query')             # узнаем, что ввел наш человечек
    if title:                                    # если название, которое он ввел, существует
        advertisements = Advertisement.objects.filter(title__icontains=title) # выводим объявления, соответсвующие запросу человечка
    else:                                        # если введенного названия нет, то
        advertisements = Advertisement.objects.all()  # выводим все объявления, которые есть
    context = {'advertisements': advertisements, 'title' : title}
    # return HttpResponse('Успешно')        # функция, возвращающая ответ "Успешно" на запрос пользователя
    return render(request, 'app_advertisement/index.html', context)    # подключение к основному коду html-шаблона, который будет определять внешний вид главной страницы сайта 

def top_sellers(request):                      # функция render отправляет что-либо на сервер(сайт) 
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {'users' : users}
    return render(request, 'app_advertisement/top-sellers.html', context)# в кавычках прописывается название файла, который необходимо отправить на сервер(сайт)

@login_required(login_url = reverse_lazy('adv_post'))                            
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisement/advertisement-post.html', context)

def advertisement_detail(request, pk): # pk позволяет показать определенное объявление с определенным id
    advertisement = Advertisement.objects.get(id=pk)
    context ={'advertisement' : advertisement}
    return render(request, 'app_advertisement/advertisement.html', context)