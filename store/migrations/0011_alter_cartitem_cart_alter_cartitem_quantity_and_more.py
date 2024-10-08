# Generated by Django 5.1.1 on 2024-09-08 12:30

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0010_alter_cart_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="store.cart",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AddConstraint(
            model_name="cartitem",
            constraint=models.UniqueConstraint(
                fields=("cart", "product"), name="unique_cart_product"
            ),
        ),
    ]
