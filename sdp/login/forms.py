from django import forms
from user.models import User
from django.contrib.auth.models import User as auth_user
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



    def clean(self):
        cleaned_data = super(LoginForm,self).clean()

        my_username = cleaned_data.get("username")
        my_password = cleaned_data.get("password")

        user = authenticate(username=my_username, password=my_password)
        if user is  None:
            self.add_error('username','login failed')



class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()

        my_username = cleaned_data.get("username")
        my_password = cleaned_data.get("password")
        my_password2 = cleaned_data.get("password2")


        users = User.objects.filter(username = my_username)

        if users.exists():
            self.add_error('username','username is used!')


        if len(my_password) < 6:
            self.add_error('password','password must be 6 character long!')

        if not my_password == my_password2:
            self.add_error('password2','password not the same !')
