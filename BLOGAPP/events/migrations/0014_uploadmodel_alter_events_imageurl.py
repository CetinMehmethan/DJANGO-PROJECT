# Generated by Django 4.2.5 on 2023-11-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_events_ishome_alter_events_isactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('video', models.ImageField(upload_to='videos')),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='imageUrl',
            field=models.TextField(),
        ),
    ]
