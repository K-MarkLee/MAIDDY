# Generated by Django 4.2.16 on 2025-01-08 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("diaries", "0002_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
