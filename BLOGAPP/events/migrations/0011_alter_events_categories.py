# Generated by Django 4.2.5 on 2023-10-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_remove_events_category_events_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='categories',
            field=models.ManyToManyField(default=1, to='events.category'),
        ),
    ]
