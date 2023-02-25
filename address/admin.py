from django.contrib import admin

from .models import Address
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display=["lat","long","placemark","building","room","floor"]

admin.site.register(Address,AddressAdmin)