from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
User=get_user_model()

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        user=self.cleaned_data.get("username")
        passw=self.cleaned_data.get("password")
        val=authenticate(username=user,password=passw)
        if val is None:
            raise forms.ValidationError("User does not exists")
class SignUpForm(forms.Form):
    username=forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField()
    password1=forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        usern = self.cleaned_data.get("username")
        passw1 = self.cleaned_data.get("password1")
        passw2 = self.cleaned_data.get("password2")
        f_n = self.cleaned_data.get("first_name")
        l_n = self.cleaned_data.get("last_name")
        email1 = self.cleaned_data.get("email")
        if not (User.objects.filter(username=usern).exists()):
            if passw1 == passw2:
                User.objects.create_user(usern, email=email1, password=passw1, first_name=f_n, last_name=l_n)
                val = authenticate(username=usern, password=passw1)
                #messages.success(request="Login Sucessfull!!"+usern)

            else:
                raise forms.ValidationError("Password incorrect")
        else:
                raise forms.ValidationError("User name Already exits")

    #email = forms.EmailField(max_length=254, required=False, help_text="Required.Inform a vaild email address.")

