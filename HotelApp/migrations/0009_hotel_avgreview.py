# Generated by Django 3.0.8 on 2020-07-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0008_auto_20200711_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='AvgReview',
            field=models.IntegerField(null=True),
        ),
    ]
