# Generated by Django 3.1.2 on 2020-11-10 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201110_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 23, 7, 8, 565377)),
        ),
        migrations.AlterField(
            model_name='user_key',
            name='key',
            field=models.CharField(default='Zcqo2m2IRjNkumx', max_length=15),
        ),
    ]