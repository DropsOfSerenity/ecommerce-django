# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150527_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(default=0.0, max_digits=100, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(to='products.Product', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
