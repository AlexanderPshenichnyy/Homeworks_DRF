from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users import views, apps

app_name = apps.UsersConfig.name

urlpatterns = [
    path('payment/', views.PaymentListView.as_view(), name='payments'),
    path('v1/checkout/sessions/', views.PaymentCreateAPIView.as_view()),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
