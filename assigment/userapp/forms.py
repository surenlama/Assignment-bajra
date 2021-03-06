from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from assigment.utils import USERTYPE_CHOICES

from django.contrib.auth import get_user_model

User = get_user_model()

#Signupform
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password(Again)",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','user_type']
        #For Label tag
        labels = {  
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
        }

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    # def clean(self):
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
    #     valpwd = self.cleaned_data['password1']
    #     valrpwd = self.cleaned_data['password2']
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError("Password doesnot match")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs={"class": 'form-control'}
        self.fields["first_name"].widget.attrs={"class": 'form-control'}
        self.fields["last_name"].widget.attrs={"class": 'form-control'}   
        self.fields["email"].widget.attrs={"class": 'form-control'}             

#login


class UserAuthentiationForm(AuthenticationForm):
    class Meta:
        model = User
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs={"class": 'form-control'}
        self.fields["password"].widget.attrs= {"class": "form-control"}
        