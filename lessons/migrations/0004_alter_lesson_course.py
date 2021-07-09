# Generated by Django 3.2.5 on 2021-07-08 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_teacher'),
        ('lessons', '0003_auto_20210708_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.course', verbose_name='Курс'),
        ),
    ]