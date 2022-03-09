# Generated by Django 4.0.2 on 2022-03-09 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('description', models.CharField(default=None, max_length=256, null=True)),
                ('owner', models.ForeignKey(default='None', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=256)),
                ('title', models.CharField(max_length=128)),
                ('artist', models.CharField(max_length=32)),
                ('duration', models.IntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tribes.playlist')),
            ],
        ),
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tribes.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=512)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tribes.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('logo', models.FileField(null=True, upload_to='')),
                ('genre', models.CharField(default=None, max_length=32, null=True)),
                ('chieftain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='tribe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tribes.tribe'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tribe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tribes.tribe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
