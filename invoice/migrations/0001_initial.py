# Generated by Django 2.2.10 on 2021-11-23 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0006_auto_20211120_1058'),
        ('sales_order', '0004_auto_20211119_1752'),
        ('pre_sales_order', '0002_auto_20211120_2320'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0004_auto_20210926_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('total_price', models.FloatField(default=0.0)),
                ('sub_total_price', models.FloatField(default=0.0)),
                ('discount_persentage', models.FloatField(default=0.0)),
                ('issued_date', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=1)),
                ('po_no', models.CharField(blank=True, max_length=12)),
                ('invoice_pdf', models.FileField(blank=True, null=True, upload_to='core/static/assets/documents/invoice/')),
                ('description', models.TextField(blank=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('total_price', models.FloatField(default=0.0)),
                ('invoice_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Product')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='product_ids',
            field=models.ManyToManyField(blank=True, null=True, to='invoice.Invoice_Product'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='related_pso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pre_sales_order.PreSalesOrder'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='related_so',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales_order.SalesOrder'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]