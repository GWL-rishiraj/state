# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'Active', help_text=b'Status of the entity', max_length=20, choices=[(b'Paused', b'Paused'), (b'Draft', b'Draft'), (b'Active', b'Active')])),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='items',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2017, 1, 12, 6, 24, 15, 145009, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2017, 1, 12, 6, 24, 23, 849534, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='slug',
            field=models.SlugField(default=' ', unique=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='status',
            field=models.CharField(default=b'Active', help_text=b'Status of the entity', max_length=20, choices=[(b'Paused', b'Paused'), (b'Draft', b'Draft'), (b'Active', b'Active')]),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_type',
            field=models.CharField(max_length=20, verbose_name=b'verbose item type', choices=[(b'M', b'menufectured'), (b'P', b'dealers'), (b'S', b'Stock')]),
        ),
        migrations.AlterField(
            model_name='items',
            name='sku',
            field=models.IntegerField(help_text=b'Unique SKU for products', verbose_name=b'verbos item', db_index=True),
        ),
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.ManyToManyField(to='items.ItemCategories', verbose_name=b'Item Categories'),
        ),
    ]
