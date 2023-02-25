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
from address.models import Address, UserAddress


class OrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    schema=OrderSchema()

    def get(self, request):
        items=Order.objects.filter(customer=request.user)
        serializer = OrderSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        global user_address
        global payment_phone
        data = request.data
        # print(data)

        # Create address from request data
        try:
            if 'address' in data:
                # Create address
                location = data["address"]
                lat= location["lat"]
                long=location["long"]
                building=location["building"]
                floor=location["floor"]
                room=location["room"]

                address = Address.objects.create(lat=lat, long=long, building=building, floor=floor, room=room)
                if address:
                    user_address = UserAddress.objects.create(address=address, user=request.user)
        except:
            user_address=Address.objects.filter(user=request.user,isDefault=True).first()


        # Payment details
        try:
            if data.get('phone'):
                payment_phone=data["phone"]
            else:
                payment_phone = request.user.phone

            # Initiate payment
            # TODO! do payment

            # Save each item in order as order
            items = data["items"]

            for item in items:
                product = get_object_or_404(Product, id=item["product"])

                if product and product.quantity >= item.quantity:
                    order = Order.objects.create(item=product, quantity=item["quantity"],
                                                 delivery_address=user_address, customer=request.user,
                                                 note=data["note"])
                    order.save()
                    product.stock -= item["quantity"]
                    product.save()

                    return Response(status=status.HTTP_201_CREATED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        data=request.data
        item=get_object_or_404(Order,id=data["item"])

        if item:
            # Check if location changed
            try:
                if 'address' in data:
                    # Create address
                    location = data["address"]
                    lat = location["lat"]
                    long = location["long"]
                    building = location["building"]
                    floor = location["floor"]
                    room = location["room"]
                    address = Address.objects.get_or_create(lat=lat, long=long, building=building, floor=floor, room=room)[0]

                    if address:
                        user_address = UserAddress.objects.get_or_create(address=address,user=request.user)[0]
                        item.delivery_address=user_address
            except:
                pass

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
