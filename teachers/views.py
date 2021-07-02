from django.views.generic import ListView, DetailView
from .models import Teacher


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'
    template_name = 'teachers/teacher_list.html'


class TeacherDetailView(DetailView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'teachers/teacher_detail.html'