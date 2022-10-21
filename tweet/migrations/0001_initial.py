# Generated by Django 4.1.2 on 2022-10-21 09:01

from django.db import migrations, models
import tweet.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(max_length=255, storage=tweet.models.OverwriteStorage(), upload_to=tweet.models.rename_imagefile_to_uuid)),
            ],
        ),
    ]
