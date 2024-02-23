from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('payed_lesson', 'payed_course')
    ordering_fields = ('date_of_payment',)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    default_serializer = UserSerializer
    queryset = User.objects.all()

    perms_methods = {
        'create': [AllowAny],
        'update': [IsAuthenticated],
        'partital_update': [IsAuthenticated],
        'destroy': [IsAuthenticated, IsAdminUser],
    }
