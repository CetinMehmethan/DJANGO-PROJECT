# Generated by Django 4.2.5 on 2023-10-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_events_category_alter_events_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]