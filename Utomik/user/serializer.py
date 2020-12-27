from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import User, Game, PlaySession

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from datetime import date



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'birth_date', 'email', 'last_played')
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class PlaySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaySession
        fields = '__all__'