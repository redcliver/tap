# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_adicional_bas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bas',
            new_name='bases',
        ),
    ]