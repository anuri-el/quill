from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
            'class': 'form-field p-3 rounded-md bg-gray-100 text-gray-800'
        }))
    first_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
            'class': 'form-field p-3 rounded-md bg-gray-100 text-gray-800'
        }))
    last_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
            'class': 'form-field p-3 rounded-md bg-gray-100 text-gray-800'
        }))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={
        'type': 'date', 
        'class': 'form-field p-3 rounded-md bg-gray-100 text-gray-800'
        }))
    phone = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
            'class': 'form-field p-3 rounded-md bg-gray-100 opacity-10 text-gray-800'
        }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-field p-3 rounded-md bg-gray-100 opacity-10 text-gray-800'
        }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'phone', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-field p-3 rounded-md bg-gray-100 text-gray-800'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-field p-3 rounded-md bg-gray-100 text-gray-800'
        })