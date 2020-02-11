from django.contrib.auth import get_user_model
from rest_framework import viewsets

from core.models import Grade, Course
from core.serializers import GradeSerializer, CourseSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class GradeViewSet(viewsets.ModelViewSet):
    filterset_fields   = ['user', 'value', 'date_added', 'course']
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer