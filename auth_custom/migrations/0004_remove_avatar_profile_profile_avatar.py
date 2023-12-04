# Generated by Django 4.2.6 on 2023-10-23 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth_custom", "0003_remove_profile_avatar_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="avatar",
            name="profile",
        ),
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="avatar",
                to="auth_custom.avatar",
            ),
        ),
    ]
