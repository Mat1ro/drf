# Generated by Django 5.2 on 2025-04-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_amount_payments_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_type',
            field=models.CharField(choices=[('cash', 'Наличка'), ('transfer', 'Перевод')], max_length=20),
        ),
    ]
