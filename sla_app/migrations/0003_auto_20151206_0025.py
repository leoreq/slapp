# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sla_app', '0002_auto_20151124_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, related_name='company', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
