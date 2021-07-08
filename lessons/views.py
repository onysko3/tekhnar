from django.views.generic import ListView, DetailView
from .models import Lesson


# class LessonListView(ListView):
#     model = Lesson
#     queryset = Lesson.objects.filter()


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'

