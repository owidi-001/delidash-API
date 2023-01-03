from django import forms

from product.models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "unit","unit_price", "image", "description", "stock"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "icon"]
