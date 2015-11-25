# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from django.contrib.postgres.operations import HStoreExtension

import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('service', models.CharField(unique=True, max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('service', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('company', models.ForeignKey(to='sla_app.Company')),
            ],
            options={
                'ordering': ('company', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('client', models.CharField(unique=True, max_length=30)),
                ('agreement_list', django.contrib.postgres.fields.hstore.HStoreField()),
                ('status', models.BooleanField(default=False)),
                ('provider', models.ForeignKey(to='sla_app.Provider')),
            ],
        ),
    ]
