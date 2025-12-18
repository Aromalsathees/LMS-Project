from rest_framework import serializers
from .models import *
from adviser_pannel .models import *


class CreateCourseSerializer(models.Model):
    class Meta:
        model = Courses
        fields = '__all__'

class EnrolledStudentSerializer(models.Model):
    class Meta:
        model = Course_Enrolled_students
        fields = '__all__'
