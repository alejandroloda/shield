# Generated by Django 3.0.5 on 2020-05-06 15:27
from django.utils.text import slugify

from django.db import migrations


def update_slugs(apps, schema_editor):
    Team = apps.get_model("metahumans", "Team")

    for team in Team.objects.all():
        team.slug = slugify(team.name)
        team.save()


def undo_update_slugs(apps, schema_editor):
    Team = apps.get_model("metahumans", "Team")
    for team in Team.objects.all():
        team.slug = None
        team.save()


class Migration(migrations.Migration):
    dependencies = [
        ('metahumans', '0009_auto_20200506_1621'),
    ]

    operations = [
        migrations.RunPython(update_slugs, undo_update_slugs)
    ]