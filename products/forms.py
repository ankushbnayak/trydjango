from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
class ProductForm(forms.Form):
    name=forms.CharField(max_length=20,widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your name'}))
    income=forms.IntegerField(widget=forms.NumberInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your income' }))
    marital_status=forms.CharField(widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your marital status'}))
    employment_status= forms.CharField(widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your employment status'}))
    graduate=forms.BooleanField(widget=forms.CheckboxInput(
            attrs={ 'style':'width:25px;height:25px;margin:10px;' }))
    dependants=forms.IntegerField(widget=forms.NumberInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter number of dependants' }))
         
class SignupForm(UserCreationForm):
    username=forms.CharField(max_length=20,widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your name'}))
    password1=forms.CharField(label=_('Password'),widget=forms.PasswordInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter password','name':'Password' }))
    password2=forms.CharField(label=_('Password Confirmation'),widget=forms.PasswordInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter password' }))
    sex=forms.CharField(widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter sex'}))
    DOB= forms.DateField(widget=forms.DateInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your date of birth'}))
    phone_number=forms.IntegerField(widget=forms.NumberInput(
             attrs={'class' : 'form-control', 'placeholder' : 'Enter your phone number'}))
    city=forms.CharField(widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter city' }))
    class Meta():
            model=User
            fields=["username","password1","password2","sex","DOB","phone_number","city"]
  
    

