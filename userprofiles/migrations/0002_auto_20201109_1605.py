# Generated by Django 3.1.2 on 2020-11-09 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofiles',
            old_name='emaild',
            new_name='emailid',
        ),
    ]