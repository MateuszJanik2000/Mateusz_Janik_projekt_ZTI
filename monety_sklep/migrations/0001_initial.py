# Generated by Django 3.1.4 on 2020-12-03 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('taken', models.BooleanField()),
                ('description', models.CharField(max_length=40000)),
                ('price', models.FloatField()),


            ],
        ),
    ]
