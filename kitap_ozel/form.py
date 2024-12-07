from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput, label="Password")
        password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

        class Meta:
            model = User
            fields = ['username', 'email']

        # Şifrelerin eşleştiğinden emin olun
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            password_confirm = cleaned_data.get("password_confirm")

            if password != password_confirm:
                raise forms.ValidationError("The passwords do not match")
            return cleaned_data