# Generated by Django 4.0.3 on 2022-03-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_orderaddress_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddress',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
