from django.urls import path
from .views import TeacherListView, TeacherDetailView


urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher_list'),
    path('<slug:slug>/', TeacherDetailView.as_view(), name='teacher_detail'),
]