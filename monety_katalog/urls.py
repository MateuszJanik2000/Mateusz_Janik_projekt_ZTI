from django.urls import path
from . import views

urlpatterns = [
    path('', views.coin_view_katalog),
    path('search/', views.monety_katalog_search, name='monety_katalog_search'),
    path('my-coins/', views.moje_monety, name='moje_monety'),
    path('posiadane_monety/<int:coin_id>/', views.posiadane_monety, name='posiadane_monety'),
]