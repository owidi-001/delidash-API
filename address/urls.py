from django.urls import path
from .views import AddressView

urlpattern=[
    path('',AddressView.as_view(),name='address'),
]