# Generated by Django 3.2.5 on 2021-09-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_alter_lesson_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='homework_example',
            field=models.URLField(blank=True, null=True, verbose_name='Посилання на відеорозбір ДЗ'),
        ),
    ]
