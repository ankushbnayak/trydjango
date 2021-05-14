from django import forms

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
    
  
    

