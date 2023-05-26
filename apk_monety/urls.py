"""apk_monety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from pay import views as pay_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sklep/', include('monety_sklep.urls')),
    path('katalog/', include('monety_katalog.urls')),
    path('pay/', pay_views.pay, name='pay'),
    path('signup/', core_views.signup, name='signup'),
    path('logout/', core_views.logout_view, name='logout'),
    path('login/', core_views.login_view, name='login'),
    path('', include('core.urls')),

]


