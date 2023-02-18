from django import forms
from .models import MainUser
from django.contrib.auth.forms import UserCreationForm


class MainUserCreateForm(UserCreationForm):
    class Meta:
        model = MainUser
        fields = ('email', 'first_name', 'last_name', 'employee_id')

    def clean(self):
        email = self.cleaned_data['email']
        if MainUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already taken.')

        employee_id = self.cleaned_data['employee_id']
        if MainUser.objects.filter(employee_id=employee_id).exists():
            raise forms.ValidationError('This employee ID is already taken.')

        return self.cleaned_data
