# Generated by Django 3.2.5 on 2021-07-09 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_alter_lesson_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['created'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
    ]
