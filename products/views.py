from django.shortcuts import redirect, render
from .models import Product,Signup
from .forms import ProductForm,SignupForm
from sklearn.preprocessing import StandardScaler
from subprocess import run,PIPE
import sys
from django.contrib.auth import login,authenticate
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np
# Create your views here.

def product_create_view(request):
    print("A")
    form =ProductForm(request.GET)
    
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
    form=ProductForm(request.POST)
    if form.is_valid():
            print("A")
            Product.objects.create(**form.cleaned_data)
    knn=joblib.load('knn.sav')

    cls = joblib.load('finalmodels.sav')
    lis=[]
    lis.append(request.POST.get('dependants', 0))
    lis.append(request.POST.get('applicant_income', 0))
    lis.append(request.POST.get('coapplicant_income', 0))
    lis.append(request.POST.get('loan_amount', 0))
    lis.append(str(int(request.POST.get('Loan_Amount_Term', 0))*365))
    lis.append(1.0)
    lis.append(request.POST.get('gender', 0))
        
    lis.append(request.POST.get('married', 0))
       
    lis.append(request.POST.get('graduate', 0))
       
    lis.append(request.POST.get('self_employed', 0))
       
    lis.append(request.POST.get('semi_urban', 0))
    lis.append(request.POST.get('urban', 0))
    print(lis)

    scaler = StandardScaler()
    features=np.array(lis)
    features = scaler.fit_transform(features.reshape(-1, 1))
    features=features.flatten()
    print(features)
    knn_ans=knn.predict([features])
    print(knn_ans)
    lis=[]

    lis.append(request.POST.get('married', 0))
       
    lis.append(request.POST.get('graduate', 0))
    lis.append(request.POST.get('dependants', 0))
    lis.append(request.POST.get('self_employed', 0))
    lis.append(request.POST.get('applicant_income', 0))
    lis.append(request.POST.get('coapplicant_income', 0))
    lis.append(request.POST.get('semi_urban', 0))
    lis.append(request.POST.get('urban', 0))
    lis.append(str(int(request.POST.get('Loan_Amount_Term', 0))*365))
    lis.append(1.0)
    print(lis)
    ans=cls.predict([lis])

    knn_ans=str(knn_ans).lstrip('[').rstrip(']')
    print(knn_ans)
    if(knn_ans=='1'):
       ans=str(ans).lstrip('[').rstrip(']')
       res=1
       ans=float(ans)

    else:
       ans="Sorry! You are not eligible for the loan"
       res=0
    print(ans)
    return render(request,'product/result.html',{'ans':round(ans),'result':res})