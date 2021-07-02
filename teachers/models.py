from django.utils.safestring import mark_safe
from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    first_name = models.CharField('Ім\'я', max_length=50)
    last_name = models.CharField('Прізвище', max_length=50)
    slug = models.SlugField('Слаг', unique=True, help_text='Посилання на латиниці. Приклад: imya-familiya')
    phone = models.CharField('Номер телефона', max_length=20, help_text='У форматі +380 (хх) ххх-хх-хх')
    email = models.EmailField('Електронна пошта')
    bio = models.TextField('Біографія')
    avatar = models.ImageField('Фото', upload_to='teachers/')

    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'

    def display_bio_safe(self):
        if '<script>' in self.bio:
            return self.bio
        return mark_safe(self.bio)

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
