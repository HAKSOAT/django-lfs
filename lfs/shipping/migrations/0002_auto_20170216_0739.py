# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-16 07:39
from __future__ import unicode_literals

from django.db import migrations


def update_price_calculator(apps, schema_editor):
    ShippingMethod = apps.get_model("shipping", "ShippingMethod")
    for shipping_method in ShippingMethod.objects.filter(price_calculator="lfs.shipping.NetShippingMethodPriceCalculator"):
        shipping_method.price_calculator = "lfs.shipping.calculator.NetPriceCalculator"
        shipping_method.save()

    for shipping_method in ShippingMethod.objects.filter(price_calculator="lfs.shipping.GrossShippingMethodPriceCalculator"):
        shipping_method.price_calculator = "lfs.shipping.calculator.GrossPriceCalculator"
        shipping_method.save()


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_price_calculator),
    ]