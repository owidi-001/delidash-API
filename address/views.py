from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from address.models import UserAddress
from address.serializers import UserAddressSerializer


# Create your views here.
class AddressView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get(self, request, format=None):
        addresses = UserAddress.objects.filter(user=request.user)
        serializer = UserAddressSerializer(addresses, many=True)

        return Response(serializer.data)