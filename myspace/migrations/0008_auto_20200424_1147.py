# Generated by Django 3.0.5 on 2020-04-24 11:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0007_category_post_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='post_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), default=[], size=None),
        ),
    ]
