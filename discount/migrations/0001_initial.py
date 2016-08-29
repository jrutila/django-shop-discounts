# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.modifiers.base
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('shop', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDiscountCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(max_length=30, verbose_name='Discount code')),
                ('cart', models.ForeignKey(to='shop.Cart', editable=False)),
            ],
            options={
                'verbose_name_plural': 'Cart discount codes',
                'verbose_name': 'Cart discount code',
            },
        ),
        migrations.CreateModel(
            name='DiscountBase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('code', models.CharField(blank=True, verbose_name='Code', max_length=30, help_text='Is discount valid only with included code')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('valid_from', models.DateTimeField(default=datetime.datetime.now, verbose_name='Valid from')),
                ('valid_until', models.DateTimeField(blank=True, null=True, verbose_name='Valid until')),
                ('num_uses', models.IntegerField(default=0, verbose_name='Number of times already used')),
                ('polymorphic_ctype', models.ForeignKey(to='contenttypes.ContentType', editable=False, related_name='polymorphic_discount.discountbase_set+', null=True)),
            ],
            options={
                'ordering': [],
                'verbose_name_plural': 'Discounts',
                'verbose_name': 'Discount',
            },
            bases=(models.Model, shop.modifiers.base.BaseCartModifier),
        ),
    ]
