# Generated by Django 5.1.4 on 2024-12-06 23:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="regions",
                        to="wildlife.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mammal",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("latin_name", models.CharField(blank=True, max_length=100, null=True)),
                ("weight", models.CharField(blank=True, max_length=50, null=True)),
                ("height", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "pregnancy_period",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("lifespan", models.CharField(blank=True, max_length=50, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("diet", models.CharField(blank=True, max_length=50, null=True)),
                ("lifestyle", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "regions",
                    models.ManyToManyField(
                        blank=True, related_name="mammals", to="wildlife.region"
                    ),
                ),
            ],
        ),
    ]
