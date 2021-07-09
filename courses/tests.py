from django.test import TestCase
from django.urls import reverse

from .models import Course
from teachers.models import Teacher


class CourseTests(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(
            first_name='John',
            last_name='Doe',
            patronymic='Vasyilevich',
            slug='john-doe',
            summary='something',
            bio='bio',
            avatar='no_photo.png'
        )
        self.course1 = Course.objects.create(
            title='course1',
            short_description='first',
            description='1 course',
            instruction='instruction1',
            subject='test1',
            start_date='2000-01-01',
            slug='course1',
            teacher=self.teacher,
            picture='no_photo.png',
            is_published=True,
        )
        self.course2 = Course.objects.create(
            title='course2',
            short_description='second',
            description='2 course',
            instruction='instruction2',
            subject='test2',
            start_date='2015-01-01',
            slug='course2',
            teacher=self.teacher,
            picture='no_photo.png',
            is_published=True,
        )

    def test_course_listing(self):
        self.assertEqual(self.course1.title, 'course1')
        self.assertEqual(self.course1.short_description, 'first')
        self.assertEqual(self.course1.description, '1 course')
        self.assertEqual(self.course1.instruction, 'instruction1')
        self.assertEqual(self.course1.subject, 'test1')
        self.assertEqual(self.course1.start_date, '2000-01-01')
        self.assertEqual(self.course1.slug, 'course1')
        self.assertEqual(self.course1.teacher, self.teacher)
        self.assertEqual(self.course1.picture, 'no_photo.png')
        self.assertTrue(self.course1.is_published)

    def test_course_list_view(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'first')
        self.assertContains(response, 'second')
        self.assertTemplateUsed(response, 'courses/course_list.html')

    def test_course_detail_view(self):
        response = self.client.get(self.course1.get_absolute_url())
        no_response = self.client.get('/courses/qwerty/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'first')
        self.assertTemplateUsed(response, 'courses/course_detail.html')

