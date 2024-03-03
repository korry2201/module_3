from django.urls import path                   # импорт объекта для связи папки и url-адреса 
from .views import index, top_sellers, advertisement_post, advertisement_detail        # импортируем функции

urlpatterns = [                                # связка функции с ответом сервера с сайтом
    path('',index, name='main_page'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('adv_post/', advertisement_post, name='adv_post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv_detail')
]