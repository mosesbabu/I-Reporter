<<<<<<< HEAD
# Generated by Django 3.0.7 on 2020-06-18 12:42

import cloudinary.models
from django.db import migrations, models
=======
# Generated by Django 3.0.7 on 2020-06-18 16:34
# Generated by Django 3.0.7 on 2020-06-18 11:52

from django.db import migrations, models
import django.utils.timezone
>>>>>>> e4429ac30d06031077a5c3986e0cd1552f5bf733


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
=======
        ('auth', '0011_update_proxy_permissions'),
>>>>>>> e4429ac30d06031077a5c3986e0cd1552f5bf733
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='picture')),
                ('bio', models.CharField(blank=True, max_length=100)),
                ('contacts', models.CharField(blank=True, max_length=30)),
            ],
=======
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
>>>>>>> e4429ac30d06031077a5c3986e0cd1552f5bf733
        ),
    ]
