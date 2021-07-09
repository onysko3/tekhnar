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

    def get_queryset(self):
        qs = super(CourseDetailView, self).get_queryset()
        return qs.filter(slug=self.kwargs['slug']).select_related('teacher')

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['has_perm'] = self.request.user.has_perm('courses.view_course', self.object)
        return context
