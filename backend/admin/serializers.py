from rest_framework import serializers
from .models import *

class CreateCourseSerializer(serializer.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class MaterialSerializer(serializer.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'
