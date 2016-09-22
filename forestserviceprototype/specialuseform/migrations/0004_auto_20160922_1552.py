# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-22 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('specialuseform', '0003_auto_20160922_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permit',
            name='organizer_name',
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_name',
            field=models.CharField(default='Permit Holder', help_text='Name of Permit Holder', max_length=250),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_signature',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='permit',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='For example: 04 28 1986'),
        ),
        migrations.AlterField(
            model_name='permit',
            name='event_name',
            field=models.CharField(help_text='The name of the event', max_length=250),
        ),
        migrations.AlterField(
            model_name='permit',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='For example: 04 28 1986'),
        ),
    ]