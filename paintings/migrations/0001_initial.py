# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('painting_name', models.CharField(max_length=100)),
                ('painting_date', models.CharField(max_length=25)),
                ('painting_cost', models.CharField(max_length=10)),
                ('painting_image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=50)),
                ('artist_type', models.CharField(max_length=25)),
                ('artist_image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='painting_artist',
            field=models.ForeignKey(to='paintings.Segment'),
        ),
    ]
