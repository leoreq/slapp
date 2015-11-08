# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        
        migrations.CreateModel(
            
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('service', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ('service', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('company', models.ForeignKey(to='sla_app.Company')),
            ],
            options={
                'ordering': ('company', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('client', models.CharField(max_length=30, unique=True)),
                ('agreement_list', django.contrib.postgres.fields.hstore.HStoreField()),
                ('status', models.BooleanField(default=False)),
                ('company', models.ForeignKey(to='sla_app.Company')),
                ('provider', models.ForeignKey(to='sla_app.Provider')),
            ],
        ),
    ]
