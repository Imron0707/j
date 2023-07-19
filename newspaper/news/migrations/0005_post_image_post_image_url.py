# Generated by Django 4.2.1 on 2023-07-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_post_previewpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(default=''),
        ),
    ]
