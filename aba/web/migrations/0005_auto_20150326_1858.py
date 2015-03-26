# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20150326_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'files/images/anuncios'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(upload_to=b'files/documents'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'files/images/noticias'),
            preserve_default=True,
        ),
    ]
