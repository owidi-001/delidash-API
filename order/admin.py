from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "item",
        "status",
        "date_ordered",
        "delivery_address",
    ]
    list_filter = ["customer",
                   "item",
                   "date_ordered",
                   "delivery_address"]


admin.site.register(Order, OrderAdmin)

