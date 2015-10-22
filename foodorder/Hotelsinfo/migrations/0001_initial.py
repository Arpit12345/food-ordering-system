# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_add', models.CharField(max_length=200)),
                ('hotel_no', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='menu_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('menu_item1', models.CharField(max_length=200)),
                ('menu_item2', models.CharField(max_length=200)),
                ('menu_item3', models.CharField(max_length=200)),
                ('menu_item4', models.CharField(max_length=200)),
                ('menu_item5', models.CharField(max_length=200)),
                ('menu_item6', models.CharField(max_length=200)),
                ('menu_item7', models.CharField(max_length=200)),
                ('menu_item8', models.CharField(max_length=200)),
                ('menu_item9', models.CharField(max_length=200)),
                ('menu_item10', models.CharField(max_length=200)),
            ],
        ),
    ]
