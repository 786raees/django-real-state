# Generated by Django 3.1.1 on 2023-01-24 10:38

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20230124_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='society_youtube_videos',
            name='yut_video_1',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
