from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework permissions import AllowAny,IsAutenticated
from .serializers import *
# Create your views hereu.


class User_Manager(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user_details = Manage_users.objects.all()
        serializer = UserDetailsSerializer(user_details ,many=True)
        return Response({'message':'The User Details has taken', 'Data':serializer.data} , status=status.HTTP_200_OK)

class Course_status(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        course_details = Course_control.objects.all()
        serializer = CourseSerializer(course_details,on_delete=models.CASCADE)
        return Response({'message':'The course data has taken successfully', 'Data':serializer.data}, status=status.HTTP_200_OK)


class Delete_course(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request,pk):
        
        try:
            get_course = Course.object.get(pk=pk)
            get_course.delete()
            return Response({'message':'The product has Deleted from Database'}, status=status.HTTP_200_OK)
        except get_course.DoesNotExist:
            return Reponse({'message':'something error happend'}, status=status.HTTP_400_BAD_REQUEST)
        
class Course_count(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        total_course_no = Courses.objects.count()
        return Response({'count':total_course}, status=status.HTTP_200_OK)


class Enrolled_students(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        students = Course_Enrolled_students.objects.all()
        serializer = EnrolledStudentSerializer(students , many=True)
        return Response({'message':'The enrolled students Data is fethed form Database' , 'Data':serializer.data}, status=status.HTTP_200_OK)