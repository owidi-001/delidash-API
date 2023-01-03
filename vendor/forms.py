from django import forms


from vendor.models import Vendor


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['brand', "tagline", "logo"]


class ShopForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['brand', "tagline", "logo"]
