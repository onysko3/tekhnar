# Generated by Django 3.2.5 on 2021-07-08 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_teacher'),
        ('lessons', '0002_auto_20210708_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Посилання на лекцію'),
        ),
    ]
