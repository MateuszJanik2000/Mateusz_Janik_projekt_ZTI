from django.contrib import admin
from . models import Coin_katal, UserCoin
# Register your models here.

@admin.register(Coin_katal)
class CoinKatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'taken')

@admin.register(UserCoin)
class UserCoinAdmin(admin.ModelAdmin):
    list_display = ['user', 'coin']
    search_fields = ['user__username', 'coin__title']

#admin.site.register(Coin_katal, CoinKatalogAdmin)