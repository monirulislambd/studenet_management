from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'password', 'photo', 'checkbox']
        labels = {'name': 'Full Name',
                  'photo': 'Upload a photo',
                  'checkbox': 'I accept the terms and conditions'}
        help_texts = {'email': 'Email should be in the format of  example@example.com'}
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'})}
        error_messages = { 'name': {'required': 'Please enter your full name.'},
                          'email': {'required': 'Please enter your e-mail address.',
                                     'invalid': 'Please enter a valid email address.',
                                     'unique': 'This email address is already taken.'},
                          'phone': {'required': 'Please enter your phone number.'},
                          'password': {'required': 'Please enter a password.'},
                          'photo': {'required': 'Please upload a photo.'},
                          'checkbox': {'required': 'Please accept the terms and conditions.'},
                          }
                                    
            