
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  title = forms.CharField(
    label='Title',
    widget=forms.TextInput(
      attrs={
        "placeholder": "Your title"
      }
    ))
  # email = forms.EmailField()
  description = forms.CharField(
    required=False,
    widget=forms.Textarea(
      attrs={
        "class": "new-class-name two",
        "rows": 20,
        "column": 120
      }
    ))
  price = forms.DecimalField()

  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price',
    ]
  #clean_<my_field_name>
  # def clean_title(self, *args, **kwargs):
  #   title = self.cleaned_data.get("title")
  #   if not "CFE" in title:
  #     raise forms.ValidationError("This is not a valid title")
  #   return title

  # def clean_email(self, *args, **kwargs):
  #   email = self.cleaned_data.get("email")
  #   if not email.endswith("com"):
  #     raise forms.ValidationError("This is not a valid email")
  #   return title

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
  # email = forms.EmailField()
