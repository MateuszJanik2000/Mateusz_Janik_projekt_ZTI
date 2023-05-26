from django.shortcuts import render, redirect
from . models import Coin_katal, UserCoin
from django.db.models import Q


def coin_view_katalog(request):
    query = request.GET.get('search')
    if query:
        monety_katalog = Coin_katal.objects.filter(Q(title__icontains=query))
    else:
        monety_katalog = Coin_katal.objects.all()
    context = {'monety_katalog': monety_katalog}
    return render(request, 'Katalog_view.html', context)


def monety_katalog_search(request):
    query = request.GET.get('q')
    if query:
        monety_katalog = Coin_katal.objects.filter(title__icontains=query)
    else:
        monety_katalog = Coin_katal.objects.all()
    context = {'monety_katalog': monety_katalog}
    return render(request, 'monety_katalog_search.html', context)

def moje_monety(request):
    user_coins = UserCoin.objects.filter(user=request.user)
    monety_katalog = [user_coin.coin for user_coin in user_coins]
    return render(request, 'moje_monety.html', {'monety_katalog': monety_katalog})

def posiadane_monety(request, coin_id):
    coin = Coin_katal.objects.get(id=coin_id)
    user_coin = UserCoin(user=request.user, coin=coin)
    user_coin.save()
    return redirect('moje_monety')