# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='pictue',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
