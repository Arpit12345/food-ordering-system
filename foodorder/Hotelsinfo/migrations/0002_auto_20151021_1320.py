# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotelsinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='hotel_no',
            field=models.IntegerField(default=0),
        ),
    ]
