# Generated by Django 3.1.7 on 2021-09-22 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolProfile', '0008_schoolprefect_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolprofile',
            old_name='next_class',
            new_name='current_class',
        ),
    ]
