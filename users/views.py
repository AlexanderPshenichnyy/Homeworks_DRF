from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_product, create_price, create_session


class PaymentListView(generics.ListAPIView):
    """
    ListView for payment
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('paid_lesson', 'paid_course')
    ordering_fields = ('date_of_payment',)


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for user
    """
    serializer_class = UserSerializer
    default_serializer = UserSerializer
    queryset = User.objects.all()

    perms_methods = {
        'create': [AllowAny],
        'update': [IsAuthenticated],
        'partital_update': [IsAuthenticated],
        'destroy': [IsAuthenticated],
    }


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        product_title = payment.paid_course.title
        amount = payment.amount
        product = create_product(product_title=product_title)
        product_price = create_price(prod_name=product, amount=int(amount))
        session_create = create_session(product_price)
        payment.url = session_create
        return payment.url
