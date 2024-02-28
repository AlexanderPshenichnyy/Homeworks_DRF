from rest_framework import serializers
from .validators import LinkValidator
from .models import Course, Lesson


# Описываем сериализатор к модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель на основе которой будет сериализатор
        model = Lesson
        # Описание полей для вывода
        fields = '__all__'
        # Валидатор ссылки
        validators = [LinkValidator(field='link')]
        serializers.UniqueTogetherValidator(fields=['link'], queryset=Lesson.objects.all())


# Описываем сериализатор к модели Course
class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course

    fields = ('title', 'preview', 'description', 'lessons_count', 'lessons')

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_subscriptions(self, obj):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=obj).exists()
