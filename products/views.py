from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from .forms import ProductForm, RawProductForm
# Create your views here.

# def product_create_view(request):
#   my_form = RawProductForm()
#   if request.method == "POST":
#     my_form = RawProductForm(request.POST)
#     if my_form.is_valid():
#       print(my_form.cleaned_data)
#       Product.objects.create(**my_form.cleaned_data)
#     else:
#       print(my_form.errors)
#   context = {
#     "form": my_form
#   }
#   return render(request, 'products/product_create.html', context)

# def product_create_view(request):
#   # print(request.GET)
#   # print(request.POST)
#   if request.method == 'POST':
#     my_new_title = request.POST.get('title')
#     print(my_new_title)
#     # Product.objects.create(title = my_new_title)
#   context = {}
#   return render(request, 'products/product_create.html', context)

def product_create_view(request):
  form = ProductForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = ProductForm()
    return redirect('/products/')
  context = {
    "form": form
  }
  return render(request, 'products/product_create.html', context)

def product_detail_view(request, id):
  obj = Product.objects.get(id=id)
  context = {
    "object": obj
  }
  return render(request, 'products/product_detail.html', context)

def dynamic_lookup_view(request, id):
  obj = get_object_or_404(Product, id=id)
  context = {
    'object': obj
  }
  return render(request, 'products/product_detail.html', context)


def product_list_view(request):
  queryset = Product.objects.all()
  context = {
    "object_list": queryset
  }
  return render(request, 'products/product_list.html', context)

#create initial data for input
def render_initial_data(request):
  initial_data = {
    'title': "My this is an awesome title"
  }
  obj = Product.objects.get(id=2)
  form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
  if form.is_valid():
    form.save()
  context = {
    "form": form
  }
  return render(request, 'products/product_create.html', context)

def product_delete_view(request, id):
  obj = get_object_or_404(Product, id=id)
  obj.delete()
  return redirect('../')
  context = {
    'object': obj
  }
  return render(request, 'products/product_delete.html', context)
