from django.shortcuts import render
from .models import Lesson
from courses.models import Course
from datetime import datetime
from guardian.decorators import permission_required_or_403


@permission_required_or_403('courses.view_course', (Course, 'slug', 'slug'))
def lesson_list(request, slug):
    lessons = Lesson.objects.filter(course__slug=slug).select_related('course').order_by('created')
    flesson = lessons[0]
    time_now = datetime.now()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons, 'flesson':flesson, 'time_now': time_now})


@permission_required_or_403('courses.view_course', (Course, 'slug', 'slug'))
def lesson_detail(request, slug, pk):
    lesson = Lesson.objects.select_related('course').get(id=pk, course__slug=slug)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})

