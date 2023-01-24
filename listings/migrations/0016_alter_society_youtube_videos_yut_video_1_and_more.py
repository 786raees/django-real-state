# Generated by Django 4.1.5 on 2023-01-24 13:07

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_alter_society_details_home_page_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='society_youtube_videos',
            name='yut_video_1',
            field=embed_video.fields.EmbedVideoField(default=None),
        ),
        migrations.AlterField(
            model_name='society_youtube_videos',
            name='yut_video_2',
            field=embed_video.fields.EmbedVideoField(default=None),
        ),
        migrations.AlterField(
            model_name='society_youtube_videos',
            name='yut_video_3',
            field=embed_video.fields.EmbedVideoField(default=None),
        ),
        migrations.AlterField(
            model_name='society_youtube_videos',
            name='yut_video_4',
            field=embed_video.fields.EmbedVideoField(default=None),
        ),
        migrations.AlterField(
            model_name='society_youtube_videos',
            name='yut_video_5',
            field=embed_video.fields.EmbedVideoField(default=None),
        ),
        migrations.AlterField(
            model_name='society_youtube_videos',
            name='yut_video_6',
            field=embed_video.fields.EmbedVideoField(default=None),
        ),
    ]
