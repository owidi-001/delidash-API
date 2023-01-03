from django import forms

from rider.models import Rider


class RiderForm(forms.ModelForm):
    class Meta:
        model=Rider
        fields=["brand","dob","gender","national_id","license"]