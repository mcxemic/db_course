# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-11 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loopModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField()),
                ('Start', models.IntegerField()),
                ('Finish', models.IntegerField()),
                ('Step', models.IntegerField()),
            ],
        ),
    ]
