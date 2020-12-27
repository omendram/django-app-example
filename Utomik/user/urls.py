from django.conf.urls import url
from django.urls import path, include
from .api import UsersApi, ListUsersLastPlayed, ListGames, FetchGame, PlaySession


urlpatterns = [
	# path('users', UsersApi.as_view()),
	# path('users/lastplayed', ListUsersLastPlayed.as_view()),
	# path('games', ListGames.as_view()),
	# path('games/<int:pk>',FetchGame.as_view()),
	# path('playsessions', PlaySession.as_view()),
]
