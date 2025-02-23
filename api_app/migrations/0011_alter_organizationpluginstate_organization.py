# Generated by Django 3.2.15 on 2022-11-12 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("certego_saas_organization", "0001_initial"),
        ("api_app", "0010_custom_config_playbooks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organizationpluginstate",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="certego_saas_organization.organization",
            ),
        ),
    ]
