# Generated by Django 4.1.5 on 2023-01-24 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_alter_city_title_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='socity_phase_sector',
            unique_together={('society', 'society_phase', 'society_sector')},
        ),
    ]
