from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'

