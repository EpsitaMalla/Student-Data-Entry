from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Admission

class StudentRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, label="Full Name")
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password validators to allow any password
        self.fields['password1'].validators = []
        self.fields['password2'].validators = []

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['name', 'email', 'message']