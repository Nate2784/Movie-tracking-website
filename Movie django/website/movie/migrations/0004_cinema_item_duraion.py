# Generated by Django 5.0.1 on 2024-02-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_rename_cinema_cinema_item_rename_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema_item',
            name='duraion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
