# Generated by Django 2.2.10 on 2022-01-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_auto_20210926_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='fax_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='mobile_number',
            field=models.IntegerField(blank=True),
        ),
    ]