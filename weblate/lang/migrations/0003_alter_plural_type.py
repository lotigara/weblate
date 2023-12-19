# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.8 on 2023-12-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lang", "0002_alter_plural_source"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plural",
            name="type",
            field=models.IntegerField(
                choices=[
                    (0, "None"),
                    (1, "One/other"),
                    (2, "One/few/other"),
                    (3, "Arabic languages"),
                    (11, "Zero/one/other"),
                    (4, "One/two/other"),
                    (14, "One/other/two"),
                    (6, "One/two/few/other"),
                    (13, "Other/one/two/few"),
                    (5, "One/two/three/other"),
                    (7, "One/other/zero"),
                    (8, "One/few/many/other"),
                    (9, "Two/other"),
                    (10, "One/two/few/many/other"),
                    (12, "Zero/one/two/few/many/other"),
                    (15, "Zero/other"),
                    (16, "Zero/one/few/other"),
                    (17, "Zero/one/two/few/other"),
                    (18, "Zero/one/two/other"),
                    (19, "Zero/one/few/many/other"),
                    (20, "One/many/other"),
                    (21, "Zero/one/many/other"),
                    (22, "One/few/many"),
                    (23, "One/zero/few/other"),
                    (666, "Unknown"),
                ],
                default=666,
                editable=False,
                verbose_name="Plural type",
            ),
        ),
    ]
