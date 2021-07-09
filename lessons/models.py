import uuid
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from courses.models import Course


class Lesson(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Опис')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='lessons')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    youtube = models.URLField('Посилання на лекцію', blank=True, null=True)
    materials = models.URLField('Посилання на матеріали', blank=True, null=True)
    homework = models.URLField('Посилання на домашнє завдання', blank=True, null=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def display_description_safe(self):
        if '<script>' in self.description:
            return self.description
        return mark_safe(self.description)

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'slug': self.course.slug, 'pk':self.id})

    def __str__(self):
        return self.title
