from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

Gender_choices=((1,'Male'),(0,'Female'),)
other_choices=((1,'Yes'),(0,'No'),)



class ProductForm(forms.Form):
    married=forms.ChoiceField(choices=other_choices,widget=forms.Select(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter marriage status' }))
    gender=forms.ChoiceField(choices=Gender_choices, widget=forms.Select(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter sex' }))
    graduate=forms.ChoiceField(choices=other_choices,widget=forms.Select(
            attrs={'class' : 'form-control', 'placeholder' : 'Graduate' }))
    dependants=forms.IntegerField(widget=forms.NumberInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter number of dependants' }))
    self_employed=forms.ChoiceField(choices=other_choices,widget=forms.Select(
            attrs={'class' : 'form-control', 'placeholder' : 'Employment' }))
    loan_amount=forms.IntegerField(widget=forms.NumberInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter loan amount' }))
    applicant_income=forms.IntegerField(widget=forms.NumberInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your income' }))
    coapplicant_income=forms.IntegerField(widget=forms.NumberInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your income' }))
    semi_urban=forms.ChoiceField(choices=other_choices,widget=forms.Select(
            attrs={'class' : 'form-control', 'placeholder' : 'semi_urban' }))
    urban=forms.ChoiceField(choices=other_choices,widget=forms.Select(
            attrs={'class' : 'form-control', 'placeholder' : 'Urban' }))
    Loan_Amount_Term=forms.IntegerField(widget=forms.NumberInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter your income' }))
    
    
         
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
  
    

