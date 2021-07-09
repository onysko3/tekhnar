from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Lesson
from teachers.models import Teacher
from courses.models import Course
from guardian.shortcuts import assign_perm


class LessonCreateMixin(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testuser123',
        )
        teacher = Teacher.objects.create(
            first_name='John',
            last_name='Doe',
            patronymic='Vasyilevich',
            slug='john-doe',
            summary='something',
            bio='bio',
            avatar='no_photo.png'
        )
        self.course = Course.objects.create(
            title='course',
            short_description='short',
            description='descr',
            subject='math',
            start_date='2000-01-01',
            slug='course',
            teacher=teacher,
            picture='no_photo.png',
            is_published=True,
        )
        self.lesson = Lesson.objects.create(
            title='text',
            description='descr',
            course=self.course,
        )
        self.course2 = Course.objects.create(
            title='course2',
            short_description='short2',
            description='descr2',
            subject='math2',
            start_date='2002-01-01',
            slug='course2',
            teacher=teacher,
            picture='no_photo.png',
            is_published=True,
        )


class CoursePerObjectPermissionTest(LessonCreateMixin, TestCase):

    def test_view_lesson_permission_restrict_no_user(self):
        response_lesson_list = self.client.get(f'/courses/{self.course.slug}/lessons/')
        response_lesson = self.client.get(self.lesson.get_absolute_url())
        self.assertEqual(response_lesson_list.status_code, 403)
        self.assertEqual(response_lesson.status_code, 403)
        self.assertFalse(self.user.has_perm('courses.view_course', self.course))

    def test_view_lesson_permission_restrict_user(self):
        self.client.login(username='testuser', password='testuser123')
        response_lesson_list = self.client.get(f'/courses/{self.course.slug}/lessons/')
        response_lesson = self.client.get(self.lesson.get_absolute_url())
        self.assertEqual(response_lesson_list.status_code, 403)
        self.assertEqual(response_lesson.status_code, 403)
        self.assertFalse(self.user.has_perm('courses.view_course', self.course))

    def test_view_lesson_permission_granted_user(self):
        assign_perm('courses.view_course', self.user, self.course)
        self.client.login(username='testuser', password='testuser123')
        response_lesson_list = self.client.get(f'/courses/{self.course.slug}/lessons/')
        response_lesson = self.client.get(self.lesson.get_absolute_url())
        self.assertTrue(self.user.has_perm('courses.view_course', self.course))
        self.assertEqual(response_lesson_list.status_code, 200)
        self.assertEqual(response_lesson.status_code, 200)
        self.assertFalse(self.user.has_perm('courses.view_course', self.course2))


class LessonTests(LessonCreateMixin, TestCase):

    def test_lesson_listing(self):
        self.assertEqual(self.lesson.title, 'text')
        self.assertEqual(self.lesson.description, 'descr')
        self.assertEqual(self.lesson.course, self.course)

    def test_lesson_list_view(self):
        assign_perm('courses.view_course', self.user, self.course)
        self.client.login(username='testuser', password='testuser123')
        response = self.client.get('/courses/' + self.course.slug + '/lessons/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'text')
        self.assertNotContains(response, 'descr')
        self.assertTemplateUsed(response, 'lessons/lesson_list.html')

    def test_lesson_detail_view(self):
        assign_perm('courses.view_course', self.user, self.course)
        self.client.login(username='testuser', password='testuser123')
        response = self.client.get(self.lesson.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'descr')
        self.assertNotContains(response, 'math')
        self.assertTemplateUsed(response, 'lessons/lesson_detail.html')