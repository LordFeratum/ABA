# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(help_text=b'Correo electronico no valido.', max_length=75),
            preserve_default=True,
        ),
    ]
