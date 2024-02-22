from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', ]
    list_filter = ['price']
    actions = ['make_auction_false', 'make_auction_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title','description'),
            'classes': ['collapse']
        }),
        ('Финанасы',{
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать все торги')
    def make_auction_false(self, request, queryset):
        queryset.update(auction = False)
    
    @admin.action(description='Проставить возможность торгов')
    def make_auction_true(self, request, queryset):
        queryset.update(auction = True)

admin.site.register(Advertisement, AdvertisementAdmin)