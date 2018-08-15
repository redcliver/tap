# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-14 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20180813_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='prod_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qnt', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto', models.ManyToManyField(to='produtos.prod')),
            ],
        ),
    ]