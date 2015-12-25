# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sla_app', '0004_auto_20151217_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='company',
            field=models.ForeignKey(to='sla_app.Company', default=1),
            preserve_default=False,
        ),
    ]
