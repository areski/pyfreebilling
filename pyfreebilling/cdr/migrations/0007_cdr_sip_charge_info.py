# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-18 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdr', '0006_auto_20171222_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdr',
            name='sip_charge_info',
            field=models.CharField(help_text='Contents of the P-Charge-Info header for billing purpose.', max_length=100, null=True, verbose_name='charge info'),
        ),
    ]
