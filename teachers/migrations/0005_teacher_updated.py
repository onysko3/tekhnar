# Generated by Django 3.2.5 on 2021-07-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_teacher_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]