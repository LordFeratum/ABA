# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20150326_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='fechaPublicacion',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='fechaPublicacion',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fechaPublicacion',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
