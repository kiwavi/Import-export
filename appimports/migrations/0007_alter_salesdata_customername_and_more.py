# Generated by Django 4.0.4 on 2022-05-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appimports', '0006_alter_salesdata_addressline1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='CUSTOMERNAME',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='ORDERDATE',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='PRODUCTCODE',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
