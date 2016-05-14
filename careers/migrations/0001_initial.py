# -*- coding: utf-8 -*-
from mezzanine.core.fields import RichTextField
from mezzanine.generic.fields import KeywordsField
from django.db import models, migrations


class Migration(migrations.Migration):

    initial=True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields = [
                ('id', models.AutoField(primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, blank=True)),
                ('title', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=2000, null=True, blank=True)),
                ('_meta_title', models.CharField(max_length=500, null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('gen_description', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=2)),
                ('publish_date', models.DateTimeField(null=True, blank=True)),
                ('expiry_date', models.DateTimeField(null=True, blank=True)),
                ('short_url', models.URLField(max_length=200, null=True, blank=True)),
                ('content', RichTextField()),
            ]
        ),
        migrations.AddField(
            model_name='jobpost',
            name='site',
            field=models.ForeignKey('sites.Site')
        ),
        migrations.AddField(
            model_name='jobpost',
            name='user',
            field=models.ForeignKey('auth.User')
        ),
    ]
