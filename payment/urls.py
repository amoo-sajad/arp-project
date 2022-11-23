from django.urls import path
from .views import (
    PaymentDetailAPIView, 
    PaymentGatewayAPIView,
    PaymentPlanListAPIView,
)

urlpatterns = [
    path('request/', PaymentGatewayAPIView.as_view(), name='payment-gateway'),
    path('detail/', PaymentDetailAPIView.as_view(), name='datail'),
    path('plans/', PaymentPlanListAPIView.as_view(), name='payment-plans'),
]
