from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.paginators import StandardResultsSetPagination
from materials.serializers import CourseSerializer, LessonSerializer
from materials.tasks import course_update


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с курсами (Course).
    Поддерживает полный CRUD (create, retrieve, update, delete).
    Использует пагинацию StandardResultsSetPagination и сериализатор CourseSerializer.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = StandardResultsSetPagination

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            course_update.delay(instance.id)
        return response


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания нового урока (Lesson).
    Доступ разрешён только аутентифицированным пользователям.
    Использует сериализатор LessonSerializer.
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    """
    Представление для получения списка всех уроков.
    Поддерживает пагинацию через StandardResultsSetPagination.
    Использует сериализатор LessonSerializer.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = StandardResultsSetPagination


class LessonDetailAPIView(generics.RetrieveAPIView):
    """
    Представление для получения детальной информации об одном уроке по его ID.
    Использует сериализатор LessonSerializer.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления информации об уроке.
    Использует сериализатор LessonSerializer.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(generics.DestroyAPIView):
    """
    Представление для удаления урока.
    """
    queryset = Lesson.objects.all()
