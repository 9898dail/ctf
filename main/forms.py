from django import forms

class UserPasswordForm(forms.Form):
    user_password = forms.CharField(max_length=256)
    