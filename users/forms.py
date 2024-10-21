from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomsUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Необязательное поле. Введите номер телефона')
    username = forms.CharField(max_length=50, required=True)
    usable_password = None

    class Meta:
        model = CustomsUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('номер телефона должен состоять только из цифр')
        return phone_number
