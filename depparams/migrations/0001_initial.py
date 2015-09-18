# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('min_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('target_article', models.OneToOneField(to='depparams.Article')),
            ],
        ),
        migrations.CreateModel(
            name='DepParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('max_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('min_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('weightage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('depreciation_curve', models.CharField(max_length=2000)),
                ('target_article', models.OneToOneField(to='depparams.Article')),
                ('target_attribute', models.OneToOneField(to='depparams.ArticleAttribute')),
            ],
        ),
    ]
