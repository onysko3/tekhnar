from django.utils.safestring import mark_safe
from django.db import models
from django.urls import reverse
from teachers.models import Teacher


class Course(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    description = models.TextField('Опис')
    slug = models.SlugField('Слаг', unique=True, help_text='Посилання на латиниці. Приклад: matematika-zno-2021')
    teacher = models.ManyToManyField(Teacher, verbose_name='Викладачі',
                                     help_text='Виберіть одного або декілька викладачів')
    picture = models.ImageField('Обкладинка', upload_to='courses/')
    is_published = models.BooleanField('Опублікувати', default=False)
    created = models.DateTimeField('Час створення', auto_now_add=True)
    updated = models.DateTimeField('Час редагування', auto_now=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курси'

    def display_description_safe(self):
        if '<script>' in self.description:
            return self.description
        return mark_safe(self.description)

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title