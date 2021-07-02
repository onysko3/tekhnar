from django.views.generic import ListView, DetailView
from .models import Course


class CourseListView(ListView):
    model = Course
    queryset = Course.objects.filter(is_published=True)
    context_object_name = 'course_list'
    template_name = 'courses/course_list.html'


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'