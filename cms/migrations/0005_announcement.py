# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150608_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=32)),
                ('author', models.CharField(unique=True, max_length=32)),
                ('slug', models.SlugField(unique=True, max_length=32)),
                ('content', models.TextField()),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
