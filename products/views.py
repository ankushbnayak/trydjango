from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_create_view(request):
    form =ProductForm(request.GET)
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
    context={
        'form':form
    }
    return render(request,'product/create.html',context)

def signup_view(request):
    return render(request,'product/signup.html')