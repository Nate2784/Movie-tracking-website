# Generated by Django 5.0.1 on 2024-02-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_rename_date_movie_year_rename_date_show_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema_item',
            name='show_time',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=10),
        ),
    ]