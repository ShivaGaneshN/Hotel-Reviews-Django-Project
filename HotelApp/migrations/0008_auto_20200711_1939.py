# Generated by Django 3.0.8 on 2020-07-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0007_auto_20200711_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Reviews',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
