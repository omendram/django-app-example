from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from datetime import date
from rest_framework.fields import CurrentUserDefault

from .models import User, Game, PlaySession



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'birth_date', 'email', 'last_played',)
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }
    
    def validate_password(self, value: str) -> str:
        return make_password(value)

    def validate_birth_date(self, dob):
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        if (not(age > 18)):
            raise serializers.ValidationError("You must be over 18 years old to register!")
        return dob


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username', 'password', 'email', 'birth_date')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class PlaySessionSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
 
    class Meta:
        model = PlaySession
        fields = '__all__'


class LastGamesPlayedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_played')

        