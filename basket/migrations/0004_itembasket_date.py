# Generated by Django 4.2.6 on 2023-11-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("basket", "0003_testbasket_itembasket"),
    ]

    operations = [
        migrations.AddField(
            model_name="itembasket",
            name="date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
