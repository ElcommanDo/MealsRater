# Generated by Django 4.0 on 2021-12-31 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together=set(),
        ),
    ]