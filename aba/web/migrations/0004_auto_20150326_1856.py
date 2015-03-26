# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_categoria_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(upload_to=b'images/documents'),
            preserve_default=True,
        ),
    ]
