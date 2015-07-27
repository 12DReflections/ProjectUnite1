# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150726_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpicture',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserPicture',
        ),
    ]
