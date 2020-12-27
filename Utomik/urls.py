from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .user.api import UsersApi, ListUsersLastPlayed, ListGames, FetchGame, ListPlaySession

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('users/', UsersApi.as_view()),
	path('users/lastplayed', ListUsersLastPlayed.as_view()),
	path('games/', ListGames.as_view()),
	path('games/<int:pk>',FetchGame.as_view()),
	path('playsessions/', ListPlaySession.as_view()),
]
