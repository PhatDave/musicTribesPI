# Generated by Django 4.0.2 on 2022-03-09 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tribes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribe',
            name='chieftain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
