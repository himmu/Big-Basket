# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigBasketApp', '0003_auto_20170216_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='featureimage',
            field=models.FileField(null=True, upload_to=b'item_images/', blank=True),
        ),
    ]
