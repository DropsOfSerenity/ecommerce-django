# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(default=29.99, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=29.99, null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
