from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework .permissions import IsAuthenticated , AllowAny
from rest_framework import status
from .serializers import *

# Create your views here.
def get_user_tokens(user):


class Admin_signup(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        try:
            serializer = SignupSerializer(data = request.data)
            if serializer.is_valid(is_admin=True):
                user = serializer.save()
                token = get_user_tokens(user)
                return Response({'message':'you have succesfully signuped' , 'user':user , 'token':token }, status=status.HTTP_201_CREATED)
            return Response({'message':'UNVALID FIELD', 'errors':user.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUETS)


class User_Signup(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        try:
            serializer = SignupSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save(is_admin=False)
                token = get_user_tokens(user) 
                return Response({'message':'you have succesfully signuped ,' 'user':user , 'token':token}, status=status.HTTP_201_CREATED)
            return Response({'message':'UNVALID FIELD', 'errors':user.errors , 'token':token}, status=status.HTTP_400_REQUEST)
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    permission_classes = [AllowAny]

    def post(self,requesst):

        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'mesage':'fill both username and password fields'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = authenticate(username=username ,password=password)
            if user is None:
                return Response({'message':'The user does not exists'}, status=status.HTTP_404_NOT_FOUND)
            token = get_user_tokens(user)
            return Response({'message':'Succsfully login', 'user':user, 'token':token},status=status.HTTP_200_OK)

class logout(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        