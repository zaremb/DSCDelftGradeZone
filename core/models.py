from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6, unique=True)
    responsibleTeacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="teacher")
    students = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f'{self.code} {self.name}'

class Grade(models.Model):
    value = models.FloatField()
    date_added = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course.code} {self.user.last_name} ({self.value})'
