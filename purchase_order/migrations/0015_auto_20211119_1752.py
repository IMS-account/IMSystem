# Generated by Django 2.2.10 on 2021-11-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0014_auto_20211102_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_pdf',
            field=models.FileField(blank=True, null=True, upload_to='core/static/assets/documents/sales order/'),
        ),
    ]
