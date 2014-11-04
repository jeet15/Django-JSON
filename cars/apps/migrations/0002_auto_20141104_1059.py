# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.FileField(upload_to=b'C:/project/sample/car/cars/media/pics/'),
            preserve_default=True,
        ),
    ]
