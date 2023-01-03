from rest_framework import serializers
from .models import User


# USERS and AUTH
class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = ["name","email","phone_number"]


# Used forms
# class ChangePasswordSerializer(serializers.Serializer):
#     """
#     Serializer for password change endpoint .
#     """

#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password reset endpoint.
    """

    email = serializers.EmailField(required=True)


class NewPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    new_password = serializers.CharField()
    short_code = serializers.IntegerField()
