from django import forms
from .models import Task
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']

class LoginForm(AuthenticationForm):
    # You can customize the form here if needed
    pass

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    error_messages = {
            'username': {
                'unique': "This username is already taken.",
                'invalid': "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.",
            },
    }