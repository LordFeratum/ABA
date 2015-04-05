# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20150404_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='latitud',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='longitud',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=10),
            preserve_default=True,
        ),
    ]
