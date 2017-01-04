# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-04 21:56
from __future__ import unicode_literals

from django.db import migrations
import money.contrib.django.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mangopay', '0003_auto_20161122_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='mangopayrefund',
            name='debited_funds',
            field=money.contrib.django.models.fields.MoneyField(decimal_places=2, default=0, max_digits=12, no_currency_field=True),
        ),
        migrations.AddField(
            model_name='mangopayrefund',
            name='debited_funds_currency',
            field=money.contrib.django.models.fields.CurrencyField(default=b'EUR', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='mangopayrefund',
            name='fees',
            field=money.contrib.django.models.fields.MoneyField(decimal_places=2, default=0, max_digits=12, no_currency_field=True),
        ),
        migrations.AddField(
            model_name='mangopayrefund',
            name='fees_currency',
            field=money.contrib.django.models.fields.CurrencyField(default=b'EUR', editable=False, max_length=3),
        ),
    ]
