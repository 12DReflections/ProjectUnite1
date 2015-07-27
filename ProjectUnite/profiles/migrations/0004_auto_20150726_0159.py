# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150726_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='pictue',
            new_name='picture',
        ),
    ]
