from django.urls import path      # импорт объекта для связи папки и url-адреса 
from .views import index          # импортируем функцию index

urlpatterns = [                   # связка функции с ответом сервера с сайтом
    path('',index)
]