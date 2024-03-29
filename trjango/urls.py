"""trjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from products.views import product_create_view,signup_view,result


urlpatterns = [
    path('',product_create_view,name='index'),
    #path('login/',auth_views.LoginView.as_view(template_name='product/login.html'),name='login'),
    path('signup/',signup_view ,name='signup'),
    path('admin/', admin.site.urls),
    path('',include("django.contrib.auth.urls")),
    path('result/',result,name="result"),
    
    

  
]
