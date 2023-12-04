# Generated by Django 4.2.6 on 2023-11-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0015_remove_product_subcategory_product_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="tags",
        ),
        migrations.AddField(
            model_name="product",
            name="limited",
            field=models.BooleanField(default=False),
        ),
    ]
