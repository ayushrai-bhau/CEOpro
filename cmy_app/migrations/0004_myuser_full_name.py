# Generated by Django 4.2.1 on 2023-05-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cmy_app", "0003_myuser_is_ceo"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="full_name",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]