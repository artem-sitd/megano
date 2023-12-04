# Generated by Django 4.2.6 on 2023-10-27 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_categoryimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryimage",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image",
                to="catalog.category",
            ),
        ),
    ]
