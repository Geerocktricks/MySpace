# Generated by Django 3.0.5 on 2020-05-07 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0011_devpost_kategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devpost',
            options={'ordering': ('publish',)},
        ),
    ]
