# Generated by Django 5.0.6 on 2025-04-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_employee_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eadd',
            field=models.CharField(max_length=100),
        ),
    ]
