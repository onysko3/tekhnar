from django.contrib import admin
from .models import Lesson
from guardian.admin import GuardedModelAdmin



class LessonAdmin(GuardedModelAdmin):
    pass


admin.site.register(Lesson, LessonAdmin)
