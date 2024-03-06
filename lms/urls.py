import lms.views
from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = LmsConfig.name

# Инициализируем объект класса DefaultRouter
router = DefaultRouter()

# Добавляем экземпляры класса DefaultRouter, роуты для ViewSet
router.register(r'course', lms.views.CourseViewSet, basename='')

urlpatterns = [
                  path('lesson/create/', lms.views.LessonCreateAPIView.as_view(), name='create_lesson'),
                  path('lesson/', lms.views.LessonListAPIView.as_view(), name='all_lessons'),
                  path('lesson/<int:pk>/', lms.views.LessonRetrieveAPIView.as_view(), name='view_lesson'),
                  path('lesson/update/<int:pk>/', lms.views.LessonUpdateAPIView.as_view(), name='update_lesson'),
                  path('lesson/destroy/<int:pk>/', lms.views.LessonDestroyAPIView.as_view(), name='delete_lesson'),
                  path('subscribe/', lms.views.SubscriptionAPIView.as_view(), name='subscribe'),
                  # path('v1/products/', lms.views.ProductAPIView.as_view()),
                  # path('v1/prices/', lms.views.PriceAPIView.as_view()),
                  path('v1/checkout/sessions/', lms.views.PaymentCreateAPIView.as_view()),
                  path('v1/payment_links/', lms.views.APIView.as_view()),

              ] + router.urls
