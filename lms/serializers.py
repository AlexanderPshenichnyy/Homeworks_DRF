from rest_framework import serializers
from lms.models import Course, Lesson


# Описываем сериализатор к модели Course


# Описываем сериализатор к модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель на основе которой будет сериализатор
        model = Lesson
        # Описание полей для вывода
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('title', 'preview', 'description', 'lessons_count', 'lessons')
