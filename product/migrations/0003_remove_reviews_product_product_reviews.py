# Generated by Django 4.2.6 on 2023-10-23 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_rename_reviews_reviews_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reviews",
            name="product",
        ),
        migrations.AddField(
            model_name="product",
            name="reviews",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.reviews",
            ),
        ),
    ]
