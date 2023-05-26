from django.db import models
from django.contrib.auth.models import User

class Coin_katal(models.Model):
    title = models.CharField(max_length= 255)
    taken = models.BooleanField()
    year = models.IntegerField()
    total = models.IntegerField()
    description = models.CharField(max_length=40000)
    picture_url = models.CharField(max_length=2083, default='')

class UserCoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin_katal, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)