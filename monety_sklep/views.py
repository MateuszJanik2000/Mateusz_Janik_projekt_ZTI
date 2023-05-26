from django.shortcuts import render
from . models import Coin


def coin_view(request):
    coin_auk = Coin.objects.all()
    return  render(request, "aukcja_view.html", {'monety_sklep':coin_auk})
