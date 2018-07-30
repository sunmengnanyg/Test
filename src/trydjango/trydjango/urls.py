"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from product.views import home_view,contact_view,about_view,product_detail_view, product_form_view, pure_view,list_view

urlpatterns = [


    url(r'^admin/', admin.site.urls),

    # url(r'^',home_view,name='home_view'),
    url(r'^home/', home_view, name='home_view'),
    url(r'^contact/',contact_view,name='contact_view'),
    url(r'^about/', about_view, name='about_view'),
    url(r'^product/', product_detail_view, name='product_view'),
    url(r'^form/', product_form_view, name='form'),
    url(r'^pure/', pure_view, name='pure'),
    url(r'^products/', list_view, name='list_view'),

]
