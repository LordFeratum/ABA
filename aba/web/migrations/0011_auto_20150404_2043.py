# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20150404_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fecha',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacto',
            name='latitud',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacto',
            name='longitud',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(help_text=b'Correo electronico no valido.', max_length=75, null=True),
            preserve_default=True,
        ),
    ]
