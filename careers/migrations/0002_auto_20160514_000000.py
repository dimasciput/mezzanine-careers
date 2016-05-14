# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):


    dependencies = [
        ('careers', '0001_initial')
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='user',
            field=models.ForeignKey('auth.User')
        ),
    ]
