from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework permissions import AllowAny,IsAutenticated
from .serializers import *
# Create your views hereu.


class Add_course(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = CreateCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'succesfully Registered new course' ,'Data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message':'something error happend' , 'error':serializer.error}, status=status.HTTP_400_BAD_REQUEST)


class Add_Materials(self,request):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk):
        try:
            get_course = Courses.object.get(pk=pk)
            get_materails = Materials.object.get(course = get_course)
            serializer = MaterialSerializer(data=get_materails)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'The materials has Added to the course {get_course}', 'Data':'serializer'})
            return Response({'message':'UNVALID FIELDS', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except get_course.DoesNotExist:
            return Response({'message':'The course Does not exists'}, status=status.HTTP_404_NOT_FOUND)
        except get_materails.DoesNotExist:
            return Response({'message':'The course Id Does Not exist , so cant add the Materials'}, status.HTTP_404_BAD_REQUEST)


class Get_course(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        get_course = Courses.objects.all()
        serializer = CreateCourseSerializer(get_course ,many=True)
        return Response({'message':'successfully fetced courses ', 'Data':serializer.data, status=status.HTTP_200_OK})


class Delete_course(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request,pk):
        
        try:
            get_course = Course.object.get(pk=pk)
            get_course.delete()
            return Response({'message':'The product has Deleted from Database'}, status=status.HTTP_200_OK)
        except get_course.DoesNotExist:
            return Reponse({'message':'something error happend'}, status=status.HTTP_400_BAD_REQUEST)
        

class Total_course(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        total_course_no = Courses.objects.count()
        return Response({'count':total_course}, status=status.HTTP_200_OK)

