# Generated by Django 3.0.7 on 2020-06-18 15:11

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IReporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='picture')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='IReporter.ProfilePic'),
        ),
    ]
