from django.urls import path
from .views import (
    PaymentDetailAPIView, 
    PaymentGatewayAPIView,
    PaymentListAPIView,
    PaymentPlanListAPIView,
    PaymentPlanCreateAPIView,
    PaymentPlanDestroyAPIView,
)

urlpatterns = [
    path('request/', PaymentGatewayAPIView.as_view(), name='payment-gateway'),
    path('detail/', PaymentDetailAPIView.as_view(), name='datail'),
    path('plans/', PaymentPlanListAPIView.as_view(), name='payment-plans'),
    path('plans/add/', PaymentPlanCreateAPIView.as_view(), name='add-plans'),
    path('plans/delete/<int:id>/', PaymentPlanDestroyAPIView.as_view(), name='delete-plans'),
    path('payments/', PaymentListAPIView.as_view(), name='payments'),
]
