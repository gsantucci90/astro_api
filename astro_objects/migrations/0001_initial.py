# Generated by Django 4.2.16 on 2024-11-07 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataRelease",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("pretty_name", models.CharField(max_length=100)),
                ("version", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="AstronomicalObject",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("right_ascension", models.FloatField()),
                ("declination", models.FloatField()),
                ("source_name", models.CharField(max_length=100)),
                (
                    "data_release",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="astro_objects.datarelease",
                    ),
                ),
            ],
        ),
    ]
