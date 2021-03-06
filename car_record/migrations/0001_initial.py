# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_datetime', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('worker', models.CharField(max_length=100, verbose_name='\u5de5\u4f5c\u8005')),
                ('job_content', models.CharField(max_length=100, verbose_name='\u5de5\u4f5c\u5185\u5bb9')),
                ('car_id', models.CharField(max_length=20, verbose_name='\u8f66\u724c\u53f7')),
                ('task_time', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u6b64\u6b21\u5de5\u65f6')),
            ],
        ),
    ]
