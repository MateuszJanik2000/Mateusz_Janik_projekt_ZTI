from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate


class SignUpForm(UserCreationForm):
    Imię = forms.CharField(max_length=30, required=True)
    Nazwisko = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text="* Pole wymagane")
    #date_of_birth = forms.DateField(input_formats=('%d-%m-%Y', '%Y-%m-%d'), help_text="DD-MM-YY format")
    #street = forms.CharField(max_length=50)
    #post_code = forms.CharField(max_length=20)
    Miasto = forms.CharField(max_length=30)
    Kraj = forms.CharField(max_length=30, help_text="* Pole wymagane")

    class Meta:
        model = User
        fields = ('username', 'Imię', 'Nazwisko', 'email', 'Miasto', 'Kraj')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        # Get the user with the given email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("Invalid login")

        # Check if the password is correct
        if not check_password(password, user.password):
            raise forms.ValidationError("Invalid login")

        return self.cleaned_data