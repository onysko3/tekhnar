from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        who = form.cleaned_data['who']
        if who == '1':
            who = 'Учень'
        elif who == '2':
            who = 'Батько'
        phone_number = form.cleaned_data['phone_number']
        try:
            send_mail('[ТЕХНАР] ЗАЯВКА НА КОНСУЛЬТАЦІЮ',
                      f'{name} {who} {phone_number}',
                      'tekhnar.zno@gmail.com',
                      ['andrukh.mykyta@student.uzhnu.edu.ua'])
        except BadHeaderError:
            return render(request, 'pages/contacts.html',
                      {'form': form, 'error': True})
        return render(request, 'pages/contacts.html',
                      {'form': form, 'success': True})
    return render(request, 'pages/contacts.html', {'form': form})
