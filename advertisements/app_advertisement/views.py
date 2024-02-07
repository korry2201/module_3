from django.http import HttpResponse        # импорт объекта response для ответа сервера клиенту
from django.shortcuts import render

def index(request):                         # функция, возвращающая ответ "Успешно" на запрос пользователя
    return HttpResponse('Успешно')

