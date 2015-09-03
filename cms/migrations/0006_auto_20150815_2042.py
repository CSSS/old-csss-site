# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
