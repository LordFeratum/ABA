# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rental'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rental',
        ),
    ]
