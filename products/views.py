from django.shortcuts import redirect, render
from .models import Product,Signup
from .forms import ProductForm,SignupForm
from subprocess import run,PIPE
import sys
from django.contrib.auth import login,authenticate
import joblib
# Create your views here.
def product_create_view(request):
    print("A")
    form =ProductForm(request.GET)
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            print("A")
            Product.objects.create(**form.cleaned_data)
    #out=run([sys.executable,'products/tests.py'],shell=False,stdout=PIPE)
    context={
        'form':form,
        #'data':out.stdout
    }
    print("Hello")
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
def result(request):
    cls = joblib.load('finalmodel.sav')
    lis=[]
    lis.append(request.POST.get('married', 0))
    lis.append(request.POST.get('graduate', 0))
    lis.append(request.POST.get('dependants', 0))
    lis.append(request.POST.get('self_employed', 0))
    lis.append(request.POST.get('applicant_income', 0))
    lis.append(request.POST.get('coapplicant_income', 0))
    lis.append(request.POST.get('semi_urban', 0))
    lis.append(request.POST.get('urban', 0))
    lis.append(request.POST.get('Loan_Amount_Term', 0))
    ans=cls.predict([lis])
    ans=str(ans).lstrip('[').rstrip(']')
    return render(request,'product/result.html',{'ans':ans})