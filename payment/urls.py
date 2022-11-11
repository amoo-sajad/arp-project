from django.urls import path
from .views import PaymentDetailAPIView, PaymentGatewayAPIView

urlpatterns = [
    path('request/', PaymentGatewayAPIView.as_view(), name='payment-gateway'),
    path('detail/', PaymentDetailAPIView.as_view(), name='datail')
]
