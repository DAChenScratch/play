# Generated by Django 2.0.3 on 2018-09-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teammember',
            options={'ordering': ['id']},
        ),
    ]
