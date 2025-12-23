from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework .permissions import IsAuthenticated , AllowAny
from rest_framework import status
from adviser_pannel .serializer import *
from adviser_pannel .models import *

# Create your views here.

class GetStudentCourses(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        course = Courses.objects.all()
        serializer = CreateCourseSerializer(course , many=True)
        return Response({'message':'All courses has fetched from Database ' , 'Data':serializer.data}, status=status.HTTP_200_OK)


class Enroll_Courses(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = EnrolledStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'The course Enrolled to the student' , 'Data':serializer.data} , status=status.HTTP_201_OK)
        return Response({'message':'error happend', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class Get_Enrolled_Courses(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            student = Course_Enrolled_students.objects.filter(student_name =request.user)
            serializer = EnrolledStudentSerializer(student , many=True)
            return Response({'message':'The Enrolled course of the student is fetched from Database', 'Data':serializer.data} , status=status.HTTP_200_OK)
        except Exception as e:

            return Response({'message':str(e)} , status=status.HTTP_400_BAD_REQUEST)
