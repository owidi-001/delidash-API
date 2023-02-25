from rest_framework import serializers

from rider.serializers import RiderSerializer
from user.serializers import UserSerializer
from vendor.serializers import VendorSerializer
from order.models import Order
from product.serializer import CategorySerializer, ProductSerializer
from address.serializers import AddressSerializer



# class OrderSerializer(serializers.ModelSerializer):
#     item = ProductSerializer()
#     delivery_address = AddressSerializer(read_only=True)
#     rider=RiderSerializer()
#     customer=UserSerializer()
#
#     class Meta:
#         model = Order
#         fields = ["id", "item", "delivery_address", "date_ordered","date_dispatched","date_delivered","quantity","status","customer","rider"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["__all__"]