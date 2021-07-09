from django.utils.safestring import mark_safe
from django.db import models
from django.urls import reverse
from teachers.models import Teacher


class Course(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    short_description = models.TextField('Короткий Опис', max_length=300)
    subject = models.CharField('Предмет', max_length=50)
    start_date = models.DateField('Початок')
    description = models.TextField('Опис')
    instruction = models.TextField('Інструкція', help_text='Відображається на закритій сторінці всіх уроків курсу')
    slug = models.SlugField('Слаг', unique=True, help_text='Посилання на латиниці. Приклад: matematika-zno-2021')
    teacher = models.ForeignKey(Teacher, verbose_name='Викладач', on_delete=models.CASCADE, related_name='courses')
    picture = models.ImageField('Обкладинка', upload_to='courses/')
    is_published = models.BooleanField('Опублікувати', default=False)
    created = models.DateTimeField('Час створення', auto_now_add=True)
    updated = models.DateTimeField('Час редагування', auto_now=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курси'
        ordering = ['-updated', '-created']

    def display_description_safe(self):
        if '<script>' in self.description:
            return self.description
        return mark_safe(self.description)

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title