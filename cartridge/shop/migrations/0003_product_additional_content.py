# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20141227_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='additional_content',
            field=mezzanine.core.fields.RichTextField(default='', verbose_name='Additional Content', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='additional_content',
            field=mezzanine.core.fields.RichTextField(default='', verbose_name='Additional Content', blank=True),
            preserve_default=True,
        ),
    ]
