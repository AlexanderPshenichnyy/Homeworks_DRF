from rest_framework import viewsets, generics
from lms.models import Course, Lesson, Subscription
from lms.permissions import IsStaffOrOwner, IsModerator
from lms.serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from lms.paginatiors import Paginator
from rest_framework.views import APIView


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = Paginator
    perms_methods = {
        'list': [IsAuthenticated, IsModerator | IsAdminUser],
        'retrieve': [IsAuthenticated, IsStaffOrOwner | IsModerator | IsAdminUser],
        'create': [IsAuthenticated, ~IsModerator],
        'update': [IsAuthenticated, IsStaffOrOwner | IsModerator],
        'partial_update': [IsAuthenticated, IsStaffOrOwner | IsModerator],
        'destroy': [IsAuthenticated, IsStaffOrOwner | IsAdminUser],
    }

    def get_permissions(self):
        self.permission_classes = self.perms_methods.get(self.action, self.permission_classes)
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permisson_classes = [IsAuthenticated, IsModerator | IsAdminUser]
    pagination_class = Paginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsStaffOrOwner | IsModerator | IsAdminUser]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsStaffOrOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsStaffOrOwner]


class SubscriptionAPIView(APIView):
    def post(self, request):
        user = request.user
        course_id = request.data.get('course_id', None)
        if course_id is not None and user.is_authenticated:
            course = Course.objects.get(pk=course_id)
            try:
                subscription = Subscription.objects.get(user=user, course=course)
                subscription.delete()
                return Response({"message": "Подписка удалена"})
            except Subscription.DoesNotExist:
                Subscription.objects.create(user=user, course=course)
                return Response({"message": "Подписка добавлена"})
        else:
            return Response({"message": "Не удалось выполнить действие"}, status=status.HTTP_400_BAD_REQUEST)
