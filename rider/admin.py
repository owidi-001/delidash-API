from django.contrib import admin

# Register your models here.

from .models import Rider


class RiderAdmin(admin.ModelAdmin):
    list_filter = ['user','brand' ,'license','national_id']
    list_display = ['user', "license",'national_id']
    search_fields = ["license"]

admin.site.register(Rider, RiderAdmin)
