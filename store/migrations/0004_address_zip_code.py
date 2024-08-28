# Generated by Django 5.1 on 2024-08-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_add_slug_to_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="zip_code",
            field=models.CharField(default="-", max_length=255),
            preserve_default=False,
        ),
    ]
