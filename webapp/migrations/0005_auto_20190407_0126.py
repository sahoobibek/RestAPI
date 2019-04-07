# Generated by Django 2.0.2 on 2019-04-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190404_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='category',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
