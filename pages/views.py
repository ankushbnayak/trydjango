from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})
def Contact_view(request,*args,**kwargs):
    my_context={
        "Name":"Ankush",
        "Number":1234,
        "List":[123,345,678]
    }
    return render(request,"contact.html",my_context)
