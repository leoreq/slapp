# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdd', '0004_list_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='text',
        ),
    ]
