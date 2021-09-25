from django import forms


class ContactForm(forms.Form):
    WHO_CHOICES = (
        ('1', 'Учень'),
        ('2', 'Батько'),
    )

    name = forms.CharField(max_length=150, label='Ім`я')
    who = forms.ChoiceField(choices=WHO_CHOICES, label='Хто ви?')
    phone_number = forms.CharField(max_length=20, label='Номер телефону')
