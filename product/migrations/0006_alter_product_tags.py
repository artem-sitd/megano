# Generated by Django 4.2.6 on 2023-10-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tags", "0001_initial"),
        ("product", "0005_remove_product_tags_product_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(blank=True, to="tags.tags"),
        ),
    ]
