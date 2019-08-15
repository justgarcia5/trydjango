
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price',
    ]

class RawProductForm(forms.Form):
  title = forms.CharField(
    label='Product title',
    widget=forms.TextInput(
      attrs={
        "placeholder": "Your title"
      }
    ))
  description = forms.CharField(
    required=False,
    widget=forms.Textarea(
      attrs={
        "class": "new-class-name two",
        "id": "my-id-fortestaera",
        "rows": 20,
        "column": 120
      }
    ))
  price = forms.DecimalField(initial=199.99)
