from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PersonalInfo, Address
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Kullanıcı Adı', max_length=150)
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput)

class CartForm(forms.Form):
    username = forms.CharField(label='Kullanıcı Adı', max_length=150)
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput)

class ProfileForm(forms.Form):
        username = forms.CharField(label='Kullanıcı Adı', max_length=150)
        password = forms.CharField(label='Şifre', widget=forms.PasswordInput)




class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Şifre", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Şifre (Tekrar)", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




#class LoginForm(forms.Form):
 #   username = forms.CharField(label="Kullanıcı Adı", max_length=100)
  #  password = forms.CharField(widget=forms.PasswordInput)

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




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['stock'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class Profile(forms.ModelForm):
    user_email = forms.EmailField(required=False, label="Email")

    class Meta:
        model = PersonalInfo
        fields = ['name', 'surname', 'phone', 'gender', 'user_email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['user_email'].initial = self.user.email


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'district', 'neighborhood', 'street', 'building_number', 'floor', 'postal_code', 'country']


class UsernameOnlyForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class PersonalInfoForm:
    pass