# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 14:42
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0003_translator_min_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='translator',
            name='too_short',
            field=models.CharField(default='Please enter at least {{page.translator.min_words}} words', max_length=160),
        ),
        migrations.AlterField(
            model_name='translator',
            name='price_word',
            field=models.DecimalField(decimal_places=5, default=Decimal('0.035'), max_digits=7),
        ),
    ]