from django.contrib.auth import get_user_model, login
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='hardpass123',
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username='adminuser',
            email='admin@email.com',
            password='hardpass123',
        )
        self.assertEqual(superuser.username, 'adminuser')
        self.assertEqual(superuser.email, 'admin@email.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class SignupTests(TestCase):

    username = 'testuser'
    email = 'testuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'РЕЄСТРАЦІЯ')
        self.assertNotContains(self.response, 'some text lalala')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class LoginTests(TestCase):

    def setUp(self):
        url = reverse('account_login')
        self.response = self.client.get(url)

    def test_login_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/login.html')
        self.assertContains(self.response, 'ВХІД')
        self.assertNotContains(self.response, 'some text')