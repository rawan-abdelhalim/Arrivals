# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150618_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='late',
            name='payment',
            field=models.IntegerField(default=10),
        ),
    ]
