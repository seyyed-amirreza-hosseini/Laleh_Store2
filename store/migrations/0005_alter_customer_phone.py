# Generated by Django 5.1 on 2024-08-29 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_address_zip_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(max_length=20),
        ),
    ]
