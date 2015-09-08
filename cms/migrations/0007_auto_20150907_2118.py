# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20150815_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='author',
            field=models.CharField(max_length=32),
        ),
    ]
