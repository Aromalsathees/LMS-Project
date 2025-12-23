from rest_framework import serializers 
from .models import *

class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username','password','email','password2','is_admin']
        extra_kwargs = {
               'password2':{'write_only':True},
               'is_admin':{'read_only':True}
        }

    def validate(self,data):
        username = data.get('username')
        password = data.get('password')
        password2 = data.get('password2')
        email = data.get('email')
        
        if not username or not password or not email or not password2:
            raise serializers.ValidationError('All fields are required')

        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError('The user already exists')
        
        if password2 != password:
            raise serializers.ValidationError('passwords not match each other')

        if len(password) < 4:
            raise serializers.ValidationError('username field must have more 3 letters')
        
            return data

    def create(self,validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    
        