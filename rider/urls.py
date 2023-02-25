from django.urls import path

from rider.views import RiderViews


urlpatterns = [
    path("rider/", RiderViews.as_view(), name="rider"),
    # path("rider/orders",RiderOrders.as_view(),name="rider_orders"),
    # path("rider/orders/accepts",RiderAcceptsOrder.as_view(),name="accepts"),
    # path("rider/orders/confirms",RiderConfirmsDelivery.as_view(),name="confirms"),
    # path("rider/orders/cancels",RiderCancelsDelivery.as_view(),name="cancels"),
]
