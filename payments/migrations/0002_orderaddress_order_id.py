# Generated by Django 3.2 on 2022-03-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderaddress',
            name='order_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
