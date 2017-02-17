"""BigBasket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
   

    url(r'^login/',csrf_exempt(Login.as_view())),
    url(r'^add-category/',csrf_exempt(Category_View.as_view())),
    url(r'^get-category',csrf_exempt(Category_View.as_view())),
    url(r'^add-sub-category/',csrf_exempt(Sub_Category.as_view())),
    url(r'^get-sub-category-by-id/',csrf_exempt(Get_Subcategory_By_Id.as_view())),
    url(r'^add-item/',csrf_exempt(Items.as_view())),
    url(r'^get-item/',csrf_exempt(Items.as_view())),
    url(r'^delete-item/',csrf_exempt(Items.as_view())),
    url(r'^get-item-by-id/',csrf_exempt(Get_Item_By_Id.as_view())),
    url(r'^update-item/',csrf_exempt(Update_Item.as_view())),
    
]
 