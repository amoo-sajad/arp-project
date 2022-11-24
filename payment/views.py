from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from expert.models import Expert
from .models import Payment, PaymentPlan
from .serializers import PaymentSerializer, PaymentPlanSerializer
import requests


def get_gateway(amount, expert_phone):
    merchant_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
    data = {
        'Amount': amount, 
        'MerchantID': merchant_id, 
        'Description': 'test',
        'Mobile': expert_phone,
        'CallbackURL': 'http://localhost:8000/payment/detail/'
    }
    r = requests.post('https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json', json=data)
    response_code = r.json()['Status']
    response_authority = r.json()['Authority']

    if r.status_code == 200 and response_code == 100:
        return {
            'status': 'success',
            'code': response_code,
            'authority': response_authority,
            'payment_gateway': 'https://sandbox.zarinpal.com/pg/StartPay/{}/'.format(response_authority),
            }

    return {'status': 'failed', 'code': '', 'payment_gateway': ''}


def verify_payment(authority, amount):
    merchant_id = '1344b5d4-0048-11e8-94db-005056a205be'
    data = {
        'MerchantID': merchant_id,
        'Authority': authority,
        'Amount': amount,
    }
    r = requests.post('https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json', json=data)

    if r.status_code == 200:
        return r.json()
    return {'status': 'failed to verify'}


class PaymentGatewayAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        expert = Expert.objects.filter(user=request.user).first()
        payment_plan = PaymentPlan.objects.get(title=request.data['payment_plan'])

        if expert:
            response = get_gateway(amount=payment_plan.price, expert_phone=expert.user.phone_number)
            payment = Payment.objects.create(
                expert=expert, 
                authority=response['authority'], 
                payment_plan=payment_plan
                )
            return Response(response)

        return Response({'unkown': 'only for experts'})


class PaymentDetailAPIView(APIView):
    def get(self, request):
        authority = request.GET.get('Authority', '')
        status = request.GET.get('Status', '')
        payment = Payment.objects.get(authority=authority)

        if status == 'OK' and payment:
            response = verify_payment(authority=authority, amount=payment.get_amount())
            if response['Status'] == 'failed to verify':
                return Response(response)
            payment.code = response['Status']
            payment.ref_id = response['RefID']
            payment.save()
            if response['Status'] == 100:
                payment.charge_expert()
            return Response(response)
        else:
            payment.delete()
            return Response({'Status': 'transaction canceled by user or failed'})


class PaymentPlanListAPIView(generics.ListAPIView):
    serializer_class = PaymentPlanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = PaymentPlan.objects.all()

