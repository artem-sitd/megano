# Generated by Django 4.2.6 on 2023-10-29 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0006_delete_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subcategory",
            name="category",
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=40)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="Родитель",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="categoryimage",
            name="category",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image",
                to="catalog.category",
            ),
        ),
    ]
