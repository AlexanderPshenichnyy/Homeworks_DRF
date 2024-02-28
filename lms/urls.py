from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView
from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = LmsConfig.name

# Инициализируем объект класса DefaultRouter
router = DefaultRouter()

# Добавляем экземпляры класса DefaultRouter, роуты для ViewSet
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
                  path('lesson/', LessonListAPIView.as_view(), name='all_lessons'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='view_lesson'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
                  path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),
              ] + router.urls
