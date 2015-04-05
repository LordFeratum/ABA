# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20150404_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='latitud',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='longitud',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
