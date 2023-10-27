# Generated by Django 4.2.6 on 2023-10-27 06:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_reviews_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
