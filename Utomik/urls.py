from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .mUtomik.api import UsersApi, ListUsersLastPlayed, ListGames, FetchGame, ApiPlaySession

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
    path('users/', UsersApi.as_view()),
	path('users/lastplayed', ListUsersLastPlayed.as_view()),
	path('games/', ListGames.as_view()),
	path('games/<int:pk>',FetchGame.as_view()),
	path('playsessions/', ApiPlaySession.as_view()),
]
