# Generated by Django 4.2.5 on 2023-10-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_events_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]