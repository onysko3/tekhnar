from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView, ContactPageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'pages/home.html')
        self.assertContains(self.response, 'Технар')
        self.assertNotContains(self.response, 'test text')

    def test_homepage_url_resolves_homepage(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'pages/about.html')
        self.assertContains(self.response, 'Технар')
        self.assertNotContains(self.response, 'test text')

    def test_aboutpage_url_resolves_aboutpage(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )


class ContactPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('contacts')
        self.response = self.client.get(url)

    def test_aboutpage(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'pages/contacts.html')
        self.assertContains(self.response, 'Технар')
        self.assertNotContains(self.response, 'test text')

    def test_aboutpage_url_resolves_aboutpage(self):
        view = resolve('/contacts/')
        self.assertEqual(
            view.func.__name__,
            ContactPageView.as_view().__name__
        )
