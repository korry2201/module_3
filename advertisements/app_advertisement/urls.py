from django.urls import path                   # импорт объекта для связи папки и url-адреса 
from .views import index, top_sellers          # импортируем функцию index

urlpatterns = [                                # связка функции с ответом сервера с сайтом
    path('',index, name='main_page'),
    path('top_sellers/', top_sellers, name='top_sellers')
]