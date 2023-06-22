from django import forms
from .models import User
from django.core.exceptions import ValidationError

"""
This form defines the fields required for user registration
"""
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name","email","phone_number", "password"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

"""
This form defines the fields required for user login
"""
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)

"""
This form defines the fields that can be updated by the user
"""
class UserUpdateForm(forms.Form):
    name = forms.CharField(
        max_length=100, help_text="Update your name",empty_value="")
    # email = forms.CharField(
    #     max_length=50, help_text="Update default email")
    # phone_number = forms.CharField(
    #     max_length=13, help_text="Update default phone number")


# Change password
class ChangePasswordForm(forms.Form):
    old_password=forms.PasswordInput()
    new_password = forms.PasswordInput()



# To be overidden
"""
This kind of computation is to be handled by the fronted
"""
class ResetPasswordForm(forms.Form):
    email = forms.CharField(
        max_length=50, help_text="Email used on registration")
        
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not (password1 == password2):
            raise ValidationError("Passwords don't match")
        return password1