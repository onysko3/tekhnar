from django.shortcuts import render
from .models import Lesson
from courses.models import Course
from datetime import datetime
from guardian.decorators import permission_required_or_403


@permission_required_or_403('courses.view_course', (Course, 'slug', 'slug'))
def lesson_list(request, slug):
    lessons = Lesson.objects.filter(course__slug=slug).order_by('created')
    time_now = datetime.now()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons, 'time_now': time_now})


@permission_required_or_403('courses.view_course', (Course, 'slug', 'slug'))
def lesson_detail(request, slug, pk):
    lesson = Lesson.objects.get(id=pk, course__slug=slug)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})

