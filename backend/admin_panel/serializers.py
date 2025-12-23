from rest_framework import serializers
from .models import *

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manage_users
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_control
        fields = '__all__'

class EnrolledStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Enrolled_students
        fields = '__all__'

class AnalystBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyst_Board
        fields = '__all__'
        