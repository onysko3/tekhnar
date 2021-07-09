from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTests(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='post title',
            description='post description',
            slug='post-slug',
        )

    def test_post_listing(self):
        self.assertEqual(self.post.title, 'post title')
        self.assertEqual(self.post.description, 'post description')
        self.assertEqual(self.post.slug, 'post-slug')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'post title')
        self.assertTemplateUsed(response, 'posts/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(self.post.get_absolute_url())
        no_response = self.client.get('/blog/qwerty/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'post description')
        self.assertTemplateUsed(response, 'posts/post_detail.html')

