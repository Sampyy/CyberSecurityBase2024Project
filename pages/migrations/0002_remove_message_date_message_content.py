# Generated by Django 5.1.2 on 2024-10-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date',
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(default='null'),
        ),
    ]
