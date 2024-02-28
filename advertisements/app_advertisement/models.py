from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# Create your models here.
# Заголовок, цена, описание, дата создания, дата обновления, уместен ли торг
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)                      # max_length - максимальное кол-во символов
    description = models.TextField('Описание')                                 # max_digit - максимальное кол-во цифр
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)        # decimal_places - мах кол-во цифр после запятой
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг будет уместен')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)       # auto_now_add - дата создания пропишется автоматически, ее нельзя будет изменить
    updated_at = models.DateTimeField('дата обновления', auto_now=True)        # auto_now - дата обновления будет автоматически обновлятся в режиме реального времени
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    @admin.display(description='Фото')
    def imageing(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;", url=self.image.url>'
            )

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.time() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weigth: bold">Сегодня в {}</span>', created_time)
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.time() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weigth: bold">Сегодня в {}</span>', updated_time)
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')
   
    def __str__(self):
        return f'Advertisement: Advertisement(id={self.id},title={self.title},price={self.price})'
    class Meta:
        db_table = 'advertisements'