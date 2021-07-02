from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contacts.html'
