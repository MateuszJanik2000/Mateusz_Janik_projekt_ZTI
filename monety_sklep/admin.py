from django.contrib import admin
from . models import Coin
# Register your models here.


class CoinAdmin(admin.ModelAdmin):
    list_display = ('title', 'taken', 'price')


admin.site.register(Coin, CoinAdmin)
