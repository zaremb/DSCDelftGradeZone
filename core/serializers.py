from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Grade, Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"