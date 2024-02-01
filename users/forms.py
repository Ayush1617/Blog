from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class NewRegisterForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'qwerty@gmail.com','class':'form-control'}))
    username = forms.CharField(required=True ,widget=forms.TextInput(attrs={'placeholder':'username','class':'form-control'}))
    password1 = forms.CharField (required=True ,widget=forms.PasswordInput({'class':'form-control'}))
    password2 = forms.CharField (required=True, widget=forms.PasswordInput({'class':'form-control'}))

    class Meta:
        model = User
        fields =("username","email","password1","password2")

    def save(self,commit=True):
        user = super(NewRegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email'] # + by using + sign  we can add some data bydefault
        if commit:
            user.save()
        return user 
        

