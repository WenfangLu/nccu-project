# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-13 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20161124_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ImageField(blank=True, null=True, upload_to='/Users/zen/nccu_project/nccu_project/nccu/nccu/menupic')),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='store',
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='comment',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
    ]
