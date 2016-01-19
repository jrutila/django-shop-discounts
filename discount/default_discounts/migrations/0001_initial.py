# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PercentDiscount',
            fields=[
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('discountbase_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='discount.DiscountBase', default=-1))
            ],
            #options={
                #'app_label': 'discount'
            #}
        ),
        migrations.CreateModel(
            name='CartItemPercentDiscount',
            fields=[
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('discountbase_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='discount.DiscountBase', default=-1))
            ],
            #options={
                #'app_label': 'discount'
            #}
        ),
        migrations.CreateModel(
            name='CartItemAbsoluteDiscount',
            fields=[
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('discountbase_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='discount.DiscountBase', default=-1))
            ],
            #options={
                #'app_label': 'discount'
            #}
        ),
    ]
