# Generated by Django 5.0.2 on 2024-02-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_post_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="photo",
            field=models.ImageField(
                default=None, upload_to="blog/media/user_post_uploads/"
            ),
        ),
    ]
