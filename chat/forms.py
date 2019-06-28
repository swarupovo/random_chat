from django import forms
# from .models import userdata


class UserRegForm(forms.Form):
    firstname = forms.CharField(label="FirstName", max_length=50)
    lastname = forms.CharField(label="LastName", max_length=50)
    username = forms.CharField(label="UserName", max_length=50)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
    email_id = forms.CharField(label="Email_Id", max_length=100, widget=forms.EmailInput)
    # gender = forms.CharField(label="GENDER", max_length=10)




class LoginForm(forms.Form):
    username = forms.CharField(label="Enter UserName:", max_length=50)
    password = forms.CharField(label="Enter Password:", max_length=50, widget=forms.PasswordInput)
