# Generated by Django 5.1 on 2025-05-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_alter_sale_amount_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='amount_change',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
