from django.contrib import admin
from .models import Course
from guardian.admin import GuardedModelAdmin


class CourseAdmin(GuardedModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
