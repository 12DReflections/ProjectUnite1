# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150726_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='picture',
        ),
    ]
