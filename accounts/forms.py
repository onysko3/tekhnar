from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',]

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class CustomSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First name',
                                 widget=forms.TextInput(attrs={'placeholder': 'Ім\'я'}))
    last_name = forms.CharField(max_length=30, label='Last name',
                                 widget=forms.TextInput(attrs={'placeholder': 'Прізвище'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
