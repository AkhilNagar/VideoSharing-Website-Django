# Generated by Django 3.2.5 on 2021-08-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210829_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default=None, null=True, upload_to='thumbnail_uploaded'),
        ),
    ]
