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
def product_detail_view(request,*args,**kwargs):
    obj=Product.objects.get(id=1)
    context={
        'Title':obj.title,
        'Description':obj.description,
        'Price':obj.price,
        'Summary':obj.summary
    }
    return render(request,'product/detail.html',context)