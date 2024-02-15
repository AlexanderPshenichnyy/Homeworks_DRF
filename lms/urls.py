from lms.apps import LmsConfig
from lms.models import Lesson, Course
from lms.views import CourseViewSet, LessonViewSet
from rest_framework.routers import DefaultRouter

app_name = LmsConfig.name

# Инициализируем объект класса DefaultRouter
router = DefaultRouter()

# Добавляем экземпляры класса DefaultRouter, роуты для ViewSet
router.register(r'course', CourseViewSet, basename='course')
router.register(r'lesson', LessonViewSet, basename='lesson')

# Добавление роутеров к пути urls.py
urlpatterns = [

               ] + router.urls
