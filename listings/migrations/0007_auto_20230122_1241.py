# Generated by Django 3.1.1 on 2023-01-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20230122_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socity_rating',
            name='rate',
            field=models.IntegerField(null=True, verbose_name={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}),
        ),
    ]
