# Generated by Django 3.1.7 on 2021-09-11 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]