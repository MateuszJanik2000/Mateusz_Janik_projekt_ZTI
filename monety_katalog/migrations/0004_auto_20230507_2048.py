# Generated by Django 3.1.4 on 2023-05-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monety_katalog', '0003_auto_20230507_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin_katal',
            name='total',
            field=models.IntegerField(),
        ),
    ]
