from rest_framework import serializers
from lms.models import Course, Lesson


# Описываем сериализатор к модели Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель на основе которой будет сериализатор
        model = Course
        # Описание полей для вывода
        fields = '__all__'


# Описываем сериализатор к модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель на основе которой будет сериализатор
        model = Lesson
        # Описание полей для вывода
        fields = '__all__'
