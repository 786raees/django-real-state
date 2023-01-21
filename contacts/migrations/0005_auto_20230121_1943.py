# Generated by Django 3.1.1 on 2023-01-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_about_team_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_members',
            name='is_mvp_team_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='team_members',
            name='is_published',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
