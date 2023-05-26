from django.db import models


class Coin(models.Model):
    title = models.CharField(max_length= 255)
    taken = models.BooleanField()
    year = models.IntegerField()
    total = models.FloatField()
    description = models.CharField(max_length=40000)
    price = models.FloatField()
    picture_url = models.CharField(max_length=2083, default='')


