# Generated by Django 5.0.1 on 2024-02-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_cinema_item_duraion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trending_movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
