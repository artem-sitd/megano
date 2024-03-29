# Generated by Django 4.2.6 on 2023-10-23 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth_custom", "0004_remove_avatar_profile_profile_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="avatar",
        ),
        migrations.AddField(
            model_name="avatar",
            name="profile",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="avatar",
                to="auth_custom.profile",
            ),
        ),
        migrations.AlterField(
            model_name="avatar",
            name="alt",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
