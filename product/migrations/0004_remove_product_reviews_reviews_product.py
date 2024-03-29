# Generated by Django 4.2.6 on 2023-10-23 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_remove_reviews_product_product_reviews"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="reviews",
        ),
        migrations.AddField(
            model_name="reviews",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.product",
            ),
        ),
    ]
