from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from order.serializers import OrderSerializer

from rider.forms import RiderForm
from order.models import Order
from rider.models import Rider
from rider.serializers import RiderSerializer


class RiderViews(APIView):
    """
    Views for rider Basic CRUD
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """
    Query all riders
    """
    def get(self,request):
        riders = Rider.objects.all()
        serializer = RiderSerializer(riders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Rider creates his brand on sign Up
    """
    def post(self, request):
        form = RiderForm(request.POST)

        if form.is_valid():
            rider=form.save(commit=False)
            rider.user=request.user

            serializer = RiderSerializer(rider)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(form.errors)
            messages.error(request,form.errors)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 


# """
# The views below manages how the rider handles order requests from accepting to
# """
# class RiderAcceptsOrder(APIView):
#     """
#     The rider accepts the order request and transits the order
#     """
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [AllowAny]
#
#     def patch(self,request):
#         item=get_object_or_404(Order,id=request.order)
#         rider=Rider.objects.get(user=request.user)
#
#         # update order details
#         item.date_dispatched=timezone.now()
#         item.rider=rider
#         item.status="Dispatched"
#
#         item.save()
#
#         serializer=OrderSerializer()
#
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
#
#
# class RiderConfirmsDelivery(APIView):
#     """
#     The rider confirms the order has been delivered to the client
#     """
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [AllowAny]
#
#
#     def patch(self,request):
#         item=get_object_or_404(Order,id=request.order)
#
#         # update order details
#         item.date_delivered=timezone.now()
#         item.status="Completed"
#
#         item.save()
#
#         serializer=OrderSerializer()
#
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
# class RiderCancelsDelivery(APIView):
#     """
#     The rider cancelles the order due to some circumstances
#     """
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [AllowAny]
#
#
#     def patch(self,request):
#         item=get_object_or_404(Order,id=request.order)
#
#         # update order details
#         item.date_delivered=None
#         item.date_dispatched=None
#         item.status="Pending"
#
#         item.save()
#
#         serializer=OrderSerializer()
#
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#


"""
Rider specific order views
"""
class RiderOrders(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    """ Gets a list of all orders belonging to the rider """

    def get(self, request):
        rider = get_object_or_404(Rider, user=request.user)
        orders=Order.objects.filter(rider=rider)

        serializer = CartItemRiderSerializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # deletes order
    def delete(self):
        order=get_object_or_404(Order,id=order)

        if order:
            OrderRider.objects.delete(order=order)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    # def patch(self,request):
    #     import json

    #     data=json.loads(request.body.decode('utf-8'))
        
    #     print(data)

    #     order=get_object_or_404(CartItem,id=data["order"])

    #     if order:
    #         print(order.product.name)

    #         order.status=data["status"]
    #         order.save()
    #         print("order saved")
    #         return Response(status=status.HTTP_202_ACCEPTED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)