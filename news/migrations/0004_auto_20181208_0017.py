# Generated by Django 2.1.4 on 2018-12-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20181207_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, upload_to='slider_image'),
        ),
    ]
