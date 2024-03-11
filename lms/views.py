from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Lesson, Subscription
from lms.paginatiors import Paginator
from lms.permissions import IsStaffOrOwner, IsModerator
from lms.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for Course"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    perms_methods = {
        'list': [IsAuthenticated, IsModerator | IsAdminUser],
        'retrieve': [IsAuthenticated, IsStaffOrOwner | IsModerator | IsAdminUser],
        'create': [IsAuthenticated, ~IsModerator],
        'update': [IsAuthenticated, IsStaffOrOwner | IsModerator],
        'partial_update': [IsAuthenticated, IsStaffOrOwner | IsModerator],
        'destroy': [IsAuthenticated, IsStaffOrOwner | IsAdminUser],
    }
    pagination_class = Paginator

    def get_permissions(self):
        self.permission_classes = self.perms_methods.get(self.action, self.permission_classes)
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    """APIView for create lesson"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    """APIView for lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permisson_classes = [IsAuthenticated, IsModerator | IsAdminUser]
    pagination_class = Paginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """APIView for lesson retrieve"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsStaffOrOwner | IsModerator | IsAdminUser]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """APIView for lesson update"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaffOrOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """APIView for lesson destroy"""
    queryset = Lesson.objects.all()
    permission_classes = [IsStaffOrOwner]


class SubscriptionAPIView(APIView):
    """APIView for Subscription"""

    def post(self, request):
        user = request.user
        course_id = request.data.get('course')
        course = get_object_or_404(Course, id=course_id)
        subscription, created = Subscription.objects.get_or_create(user=user, course=course)
        if not created:
            subscription.delete()
            message = 'Подписка удалена'
        else:
            message = 'Подписка добавлена'
        return Response({'message': message}, status=status.HTTP_200_OK)
