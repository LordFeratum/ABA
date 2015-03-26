# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'images'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'images'),
            preserve_default=True,
        ),
    ]
