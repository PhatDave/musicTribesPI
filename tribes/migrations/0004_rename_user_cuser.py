# Generated by Django 4.0.2 on 2022-03-09 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('tribes', '0003_rename_cuser_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CUser',
        ),
    ]