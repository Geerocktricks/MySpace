# Generated by Django 3.0.5 on 2020-04-24 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0005_auto_20200424_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]