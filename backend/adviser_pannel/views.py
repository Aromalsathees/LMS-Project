from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import status
from rest_framework .permissions import IsAuthenticated , AllowAny
from .serializer import *
# Create your views here.

class Create_Course(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = CreateCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'succesfully Registered new course' ,'Data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message':'something error happend' , 'error':serializer.error}, status=status.HTTP_400_BAD_REQUEST)


class Add_Materials(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk):
        try:
            get_course = Courses.object.get(pk=pk)
            get_materials = request.data.copy()
            get_materials['course'] = get_course.id

            serializer = MaterialSerializer(get_materials)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'The Materials is added to the courses', 'Data':serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'message':'UNVALID FIELD ERROR', 'error':serializer.errors}, status=status.HTTP_400_BDA_REQUEST)
        except get_course.DoesNotExists:

            return Response({'message':'The course Does NOt exist'}, status=status.HTTP_404_NOT_FOUND)

class Get_Adviser_courses(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            get_adviser = Courses.objects.filter(created_teacher_name=request.user)
            serializer = CreateCourseSerializer(get_adviser ,many=True)
            return Response({'message':'The advisers courses are taken' , 'Data':serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

