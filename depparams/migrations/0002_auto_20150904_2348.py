# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depparams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleattribute',
            name='value',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(null=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='articleattribute',
            name='description',
            field=models.CharField(null=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='depparam',
            name='description',
            field=models.CharField(null=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
