from rest_framework import serializers

from .models import Address, UserAddress


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id","lat","long","placemark", "building","floor","room"]

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ["id", "user", "address"]