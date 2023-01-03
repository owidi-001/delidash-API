from rest_framework import serializers
from rider.models import Rider
from user.serializers import UserSerializer



class RiderSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Rider
        fields = ["id", "user","brand","dob","gender","national_id","license"]