from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display=[
        "user","subject"
    ]
    list_filter=[
        "user","subject"
    ]


admin.site.register(Contact,ContactAdmin)