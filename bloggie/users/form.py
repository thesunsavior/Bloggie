from cProfile import label
import email
from unicodedata import name
from attr import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FB_User, GG_User, Profile
from allauth.socialaccount.forms import SignupForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


class FacebookAuthForm(SignupForm):

    name = forms.CharField(label="name")
    PhoneNumber = forms.CharField(label="phone number")

    # def __init__(self, sociallogin=None, **kwargs):
    #     super(FacebookAuthForm, self).__init__(**kwargs)

    class Meta:
        model = FB_User
        fields = ['name', 'phoneNumber']

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(FacebookAuthForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user


class GoogleAuthForm(SignupForm):
    role = (
        ("Student", "Student"),
        ("Teacher", "Teacher"),
        ("Other", "Other"),
    )

    name = forms.CharField(label="Name")
    occupation = forms.ChoiceField(choices=role, label="Your occupation?")

    # def __init__(self, sociallogin=None, **kwargs):
    #     super(GoogleAuthForm, self).__init__(**kwargs)

    class Meta:
        model = GG_User
        fields = ['name', 'occupation']

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(GoogleAuthForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user
