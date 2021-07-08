# Generated by Django 3.2.5 on 2021-07-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20210702_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Електронна пошта'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, help_text='У форматі +380 (хх) ххх-хх-хх', max_length=20, null=True, verbose_name='Номер телефона'),
        ),
    ]
