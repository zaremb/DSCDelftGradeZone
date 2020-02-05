from django.contrib import admin

# Register your models here.
from core.models import CustomUser, Grade, Course

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Grade)