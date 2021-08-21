from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

class RegistrationForm(UserCreationForm):
    GENDER = [
        (0, "Male"),
        (1, "Female")
    ]
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=(GENDER), widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'bio',
            'cover_pic',
            'dp'
        )