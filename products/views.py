from django.shortcuts import render
from .models import Product,Signup
from .forms import ProductForm,SignupForm
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
    form2 =SignupForm(request.GET)
    if request.method=='POST':
        form2=SignupForm(request.POST)
        if form2.is_valid():
         print("B")
         Signup.objects.create(**form2.cleaned_data)
    context={
        'form':form2
    }
    return render(request,'product/signup.html',context)
    