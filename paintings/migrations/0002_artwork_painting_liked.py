# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='painting_liked',
            field=models.BooleanField(default=False),
        ),
    ]
