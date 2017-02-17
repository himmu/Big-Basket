# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigBasketApp', '0002_auto_20170216_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='featureimage',
            field=models.FileField(null=True, upload_to=b'static/static/img/item_images', blank=True),
        ),
    ]
