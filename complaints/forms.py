from django import forms
from .models import Complaint
from django.contrib.auth.models import User
from complaints.models import TYPES_OF_COMPLAINTS
from django.contrib.auth.forms import UserCreationForm

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
        exclude = ['user', 'action_taken']
        widgets = {
            'type_of_complaint': forms.Select(choices=TYPES_OF_COMPLAINTS),
            'description': forms.Textarea(attrs={'rows': 5}),
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # Add custom CSS classes to form fields here
        self.fields['username'].widget.attrs['class'] = 'username'
        self.fields['password1'].widget.attrs['class'] = 'password'
        self.fields['password2'].widget.attrs['class'] = 'password'

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']