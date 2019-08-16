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
def render_initial_data(request, id):
  obj = Product.objects.get(id=id)
  # initial_data = {
  #   'title': obj.title,
  #   'description': obj.description,
  #   'price': obj.price
  # }
  form = ProductForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.save()
    return redirect('/products/')
  context = {
    "form": form
  }
  return render(request, 'products/product_edit.html', context)

def product_delete_view(request, id):
  obj = get_object_or_404(Product, id=id)
  obj.delete()
  return redirect('../')
  context = {
    'object': obj
  }
  return render(request, 'products/product_delete.html', context)
