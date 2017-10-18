# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_cat', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FoodDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=250)),
                ('food_price', models.IntegerField()),
                ('foodtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.Food')),
            ],
        ),
    ]
