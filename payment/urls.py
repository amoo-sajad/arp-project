from django.urls import path
from .views import (
    PaymentDetailAPIView, 
    PaymentGatewayAPIView,
    PaymentListAPIView,
    PaymentPlanListCreateAPIView,
    PaymentPlanDestroyAPIView,
)

urlpatterns = [
    path('request/', PaymentGatewayAPIView.as_view(), name='payment-gateway'),
    path('detail/', PaymentDetailAPIView.as_view(), name='datail'),
    path('plans/', PaymentPlanListCreateAPIView.as_view(), name='payment-plans'),
    path('delete/', PaymentPlanDestroyAPIView.as_view(), name='delete-plans'),
    path('payments/', PaymentListAPIView.as_view(), name='payments'),
]
