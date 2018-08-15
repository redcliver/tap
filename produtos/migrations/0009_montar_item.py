# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_auto_20180815_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='montar_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ads1', models.ManyToManyField(to='produtos.adicional')),
                ('base1', models.ManyToManyField(to='produtos.bases')),
            ],
        ),
    ]
