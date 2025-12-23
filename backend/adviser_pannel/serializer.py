from rest_framework import serializers
from .models import *

class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'
