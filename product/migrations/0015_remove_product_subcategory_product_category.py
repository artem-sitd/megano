# Generated by Django 4.2.6 on 2023-10-29 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0007_remove_subcategory_category_category_and_more"),
        ("product", "0014_remove_product_category_product_subcategory"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="subcategory",
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.category",
            ),
        ),
    ]
