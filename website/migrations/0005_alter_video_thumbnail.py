# Generated by Django 3.2.5 on 2021-08-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='thumbnail_uploaded'),
        ),
    ]
