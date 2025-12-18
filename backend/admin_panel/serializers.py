from rest_framework import serializers
from .models import *

class UserDetailsSerializer(serializer.ModelSerializer):
    class Meta:
        model = Manage_users
        fields = '__all__'

class CourseSerializer(serializer.ModelSerializer):
    class Meta:
        model = Course_control
        fields = '__all__'

class EnrolledStudentSerializer(serializer.ModelSerializer):
    class Meta:
        model = Course_Enrolled_students
        fields = '__all__'