from rest_framework import serializers 
from .models import *

class SignupSerializer(serializers.ModelSerializer):
    password2 = serializer.charField()

    class Meta:
        model = CustomUser
        fields = ['username ','password','email','password2','is_admin']
        extra_kwrags = {
               'password2':{write_only:True},
               'is_admin':{read_only:True}
        }

    def validate(self,data):
        username = data.get('username')
        password = data.get('password')
        password2 = data.get('password2')
        email = data.get('email')

        username = CustomUser.objects.filter(username=username).exists()
        if username:
            return serializer.validationError('The user already exists')
        
        if password2 != password:
            return serializers.validationError('passwords not match each other')

        if not username or not password or not email or not password2:
            return serializers.validationError('All fields are required')

        if len(password) <= 3:
            return serializers.validationError('username field must have more 3 letters')
        
    def create(self,validated_data):
        validated_data.pop('password2')
        password = validated.pop('password')

        user = CustomUser(*validated_data)
        user.set_password(password)
        user.save()
        return user

    
        