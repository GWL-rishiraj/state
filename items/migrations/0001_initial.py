# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('sku', models.IntegerField(help_text=b'Unique SKU for products')),
                ('item_type', models.CharField(max_length=20, choices=[(b'M', b'menufectured'), (b'P', b'dealers'), (b'S', b'Stock')])),
            ],
        ),
    ]
