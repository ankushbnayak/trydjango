from django.shortcuts import redirect, render
from .models import Product,Signup
from .forms import ProductForm,SignupForm
from django.contrib.auth import login,authenticate
# Create your views here.
def product_create_view(request):
    form =ProductForm(request.GET)
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            print("A")
            Product.objects.create(**form.cleaned_data)
    context={
        'form':form
    }
    return render(request,'product/create.html',context)

def signup_view(request):
    form =SignupForm(request.GET)
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect('index')
    context={
        'form':form
    }
    return render(request,'product/signup.html',context)
    