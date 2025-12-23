from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from ai_services .ai_views import *
# Create your views hereu.

# manage users views starts here
class User_Manager(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user_details = Manage_users.objects.all()
        serializer = UserDetailsSerializer(user_details ,many=True)
        return Response({'message':'The User Details has taken', 'Data':serializer.data} , status=status.HTTP_200_OK)

# Course controll view starts here 
class Course_status(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        course_details = Course_control.objects.all()
        serializer = CourseSerializer(course_details,on_delete=models.CASCADE)
        return Response({'message':'The course data has taken successfully', 'Data':serializer.data}, status=status.HTTP_200_OK)

# Delete and edit view starts here
class Delete_course(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request,pk):
        
        try:
            get_course = Course.object.get(pk=pk)
            get_course.delete()
            return Response({'message':'The product has Deleted from Database'}, status=status.HTTP_200_OK)
        except get_course.DoesNotExist:
            return Reponse({'message':'something error happend'}, status=status.HTTP_400_BAD_REQUEST)
  
# Analyst Dashboard view starts here
class Total_users(APIView):
    permission_classes = permission_classes = [IsAuthenticated]
    
    def get(self,request):
        try:
            get_users = Analyst_Board.objects.filter(total_users__user_status == 'activate')
            serializer = AnalystBoardSerializer(get_users , many=True)
            return Response({'message':'The active users are fetched from database' , 'Data':serializer.data} , status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class Active_users(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            active_courses = Analyst_Board.objects.filter(active_courses__course_status = 'approved')
            serializer = AnalystBoardSerializer(active_courses , many=True)
            return Response({'message':'The active courses are fetched from database ','Data':serializer.data} , status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_500-INTERNAL_SERVER_ERROR)


# AI services admin starts from here
class AI_Bot(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        try:
            prompt = request.data
            if len(prompt) == 0:
                return Respone({'fill the prompts'}, status=status.HTTP_400_BAD_REQUEST)
            if prompt == 'general_text':
                ai_response = call_ai(prompt)
            if prompt == 'grammer_correct':
                ai_respone = Grammer_correction(prompt)
            if prompt = 'practice_sentence':
                ai_response = practice_sentence(prompt)
            if not ai_response:
                return Response({'AI is not responding right at the moment'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':'The ai given response {ai_response}'} ,status=status.HTTP_200_OK)
        except Expection as e:
            return Response({'message':str(e)} ,status=status.HTTP_500_INTERNAL_SERVER_SERROR)

    

