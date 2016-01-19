# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_discounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitemabsolutediscount',
            name='amount',
            field=models.DecimalField(decimal_places=2, verbose_name='Amount', max_digits=5),
        ),
        migrations.AlterField(
            model_name='cartitemabsolutediscount',
            name='discountbase_ptr',
            field=models.OneToOneField(primary_key=True, to='discount.DiscountBase', auto_created=True, serialize=False, parent_link=True),
        ),
        migrations.AlterField(
            model_name='cartitempercentdiscount',
            name='amount',
            field=models.DecimalField(decimal_places=2, verbose_name='Amount', max_digits=5),
        ),
        migrations.AlterField(
            model_name='cartitempercentdiscount',
            name='discountbase_ptr',
            field=models.OneToOneField(primary_key=True, to='discount.DiscountBase', auto_created=True, serialize=False, parent_link=True),
        ),
        migrations.AlterField(
            model_name='percentdiscount',
            name='amount',
            field=models.DecimalField(decimal_places=2, verbose_name='Amount', max_digits=5),
        ),
        migrations.AlterField(
            model_name='percentdiscount',
            name='discountbase_ptr',
            field=models.OneToOneField(primary_key=True, to='discount.DiscountBase', auto_created=True, serialize=False, parent_link=True),
        ),
    ]
