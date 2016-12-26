# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-22 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab7', '0002_hostelmodel_roommodel_studentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommodel',
            name='ID_Student',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='ID',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='ID_Hostel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab7.HostelModel'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='Room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab7.RoomModel'),
        ),
    ]