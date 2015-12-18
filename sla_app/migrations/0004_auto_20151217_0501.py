# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sla_app', '0003_auto_20151206_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, to='sla_app.List'),
        ),
    ]
