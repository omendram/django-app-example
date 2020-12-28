from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models.signals import post_save
from django.dispatch import receiver


from .permissions import isStaff
from .models import User, Game, PlaySession
from .serializer import RegisterSerializer, UserSerializer, GameSerializer, PlaySessionSerializer, LastGamesPlayedSerializer


class CustomAPIView(APIView):
    def get_permissions(self):
        return {
            key: [permission() for permission in permissions] for key, permissions in self.permission_classes.items()
        }

    def check_permissions(self, request):
        method = request.method.lower()

        for permission in self.get_permissions()[method]:
            if not permission.has_permission(request, self):
                self.permission_denied(request, message=getattr(permission, 'message', None))


class UsersApi(CustomAPIView):
    permission_classes = {'get': [isStaff], 'post': [AllowAny]}
    
    def post(self, request, format=None):
        serializer = RegisterSerializer(data = request.data)
        
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)


class ListGames(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameSerializer(games, many = True)
        return Response(serializer.data)


class FetchGame(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)


class ApiPlaySession(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PlaySessionSerializer(data = request.data, context = {"request": request})

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUsersLastPlayed(APIView):
    permission_classes = [isStaff]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = LastGamesPlayedSerializer(users, many = True)

        return Response(serializer.data)


@receiver(post_save, sender=PlaySession)
def update_user(sender, instance, **kwargs):
    user = instance.created_by
    game = instance.game
    user.last_played = game
    user.save()