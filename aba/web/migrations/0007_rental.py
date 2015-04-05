# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20150328_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
