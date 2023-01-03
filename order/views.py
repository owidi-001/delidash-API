# Create your views here.
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from order.schema import OrderSchema
from product.models import Product
from .models import Order
from .serializers import OrderSerializer
from address.models import Address

class OrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    schema=OrderSchema()

    def get(self, request):
        items=Order.objects.filter(customer=request.user)
        serializer = OrderSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        
        # data={'location': {'id': -1, 'placemark': 'Njokerio Seventh Street  Njoro  Kenya', 'country': 'Njokerio Seventh Street  Njoro  Kenya', 'city': 'Njokerio Seventh Street  Njoro  Kenya', 'street': 'Njokerio Seventh Street  Njoro  Kenya', 'block': 'murira apartments ', 'floor': '3', 'room': '34c'}, 
        # 'items': [
        #     {'product': 3, 'quantity': 3}, 
        #     {'product': 4, 'quantity': 1}], 
        #     'total': 1128.0, 
        #     'phone': '0786484661'}


        # Create location from request data
        location=data["location"]
        delivery_address=Address.objects.get_or_create(
            placemark=location["placemark"],
            block = location["block"],
            floor = location["floor"],
            room = location["room"]
        )

        # Save each item in order as order
        items=data["items"]

        for item in items:
            try:
                product=get_object_or_404(Product,id=item["product"])
                if product:
                    order=Order.objects.create(item=product,quantity=item["quantity"],delivery_address=delivery_address,customer=request.user,note=data["note"])
                    order.save()
                    product.stock -= item["quantity"]
                    product.save()                    
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
        


    def patch(self,request):
        data=request.data
        item=get_object_or_404(Order,id=data["item"])

        if item:
            # Check if location changed
            if data["location"]:
                location = data["location"]
                delivery_address=Address.objects.get_or_create(
                room = location["room"],
                floor = location["floor"],
                block = location["block"],
                
                placemark=location["placemark"])

                item.delivery_address=delivery_address
            if data["status"]:
                item.status=data["status"]
            
            if data["note"]:
                item.note=data["note"]

            if data["quantity"]:
                item.quantity=data["quantity"]

            item.save()

            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = request.data
        item = get_object_or_404(Order, id=data["item"])

        if item:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
