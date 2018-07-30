from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm,PureForm

# Create your views here.

# def home_view(*args,**kwargs):
#
#     return HttpResponse("<h1>Hello DLSM's Home.</h1>")


def home_view(request,*args, **kwargs):

    return render(request,'home.html',{})

def contact_view(request,*args, **kwargs):

    return render(request,'contact.html',{})


def about_view(request,*args, **kwargs):
    context = {
        "Me": 'This is me.',
        'Number':'My number is 123.'
    }

    return render(request,'about.html',context)


def product_detail_view(request):
    obj = Product.objects.get(id=2)
    context = {
        'Title':obj.Title,
        'Summary':obj.Summary
    }

    return render(request,'product/detail.html',context)


def product_form_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form':form
    }

    return render(request,'product/form.html',context)

def pure_view(request):
    my_form = PureForm()
    if request.method == 'POST':
        my_form = PureForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.Title)
            # print(my_form.cleaned_data)
        else:
            pass
            # print(my_form.error)
    context = {
        'form':my_form
    }
    return render(request,'product/pure.html',context)

def list_view(request):
    queryset = Product.objects.all()
    context ={
        'object_list':queryset
    }
    return render(request,'product/list.html',context)