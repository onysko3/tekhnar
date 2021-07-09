from django.test import TestCase
from django.urls import reverse
from .models import Teacher


class TeacherTests(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(
            first_name='John',
            last_name='Smith',
            slug='john-smith',
            email='johnsmith@gmail.com',
            bio='I\'m John Smith',
            avatar='no_photo.jpg'
        )

    def test_teacher_listing(self):
        self.assertEqual(f'{self.teacher.first_name}', 'John')
        self.assertEqual(f'{self.teacher.last_name}', 'Smith')
        self.assertEqual(f'{self.teacher.slug}', 'john-smith')
        self.assertEqual(f'{self.teacher.email}', 'johnsmith@gmail.com')
        self.assertEqual(f'{self.teacher.bio}', 'I\'m John Smith')

    def test_teacher_list_view(self):
        response = self.client.get(reverse('teacher_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Smith')
        self.assertNotContains(response, 'some test text')
        self.assertTemplateUsed(response, 'teachers/teacher_list.html')

    def test_teacher_detail_view(self):
        response = self.client.get(self.teacher.get_absolute_url())
        no_response = self.client.get('teachers/qwerty/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'John Smith')
        self.assertNotContains(response, 'some test text')
        self.assertTemplateUsed(response, 'teachers/teacher_detail.html')
