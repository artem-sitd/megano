# Generated by Django 4.2.6 on 2023-10-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_product_specifications_product_specifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=models.ManyToManyField(null=True, to='product.specifications'),
        ),
    ]