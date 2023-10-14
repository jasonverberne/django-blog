# Generated by Django 4.2.5 on 2023-10-12 23:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogging", "0003_delete_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="post",
            name="name",
            field=models.CharField(default=2, max_length=128),
            preserve_default=False,
        ),
    ]
