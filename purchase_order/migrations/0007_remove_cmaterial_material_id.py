# Generated by Django 2.2.10 on 2021-11-01 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0006_cmaterial_po_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmaterial',
            name='material_id',
        ),
    ]