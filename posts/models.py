from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField('Слаг', unique=True, help_text='Посилання на латиниці. Приклад: zno-na-200')
    description = models.TextField('Опис')
    picture = models.ImageField(upload_to='blog/', blank=True, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

    def display_description_safe(self):
        if '<script>' in self.description:
            return self.description
        return mark_safe(self.description)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

