# Generated by Django 2.2.10 on 2022-04-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0002_auto_20220108_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='qproduct',
            name='unit_price',
            field=models.FloatField(default=0.0),
        ),
    ]
