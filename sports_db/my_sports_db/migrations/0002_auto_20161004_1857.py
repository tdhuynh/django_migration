# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 18:57
from __future__ import unicode_literals

from django.db import migrations
import csv


def add_ufc_data(apps, schema_editor):
    Fighter = apps.get_model("my_sports_db", "Fighter")
    with open('stats.csv') as open_file:
        contents = csv.reader(open_file)
        for row in contents:
            Fighter.objects.create(first_name=row[0],last_name=row[1],fights=row[2],strikes=row[3],
            strike_accuracy=row[4],takedowns=row[5],takedown_accuracy=row[6],knockdowns=row[7],passes=row[8],
            reversals=row[9],submissions=row[10])

    #raise Exception("oogly boogly")


class Migration(migrations.Migration):

    dependencies = [
        ('my_sports_db', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_ufc_data)
    ]
