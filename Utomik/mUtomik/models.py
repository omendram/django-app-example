from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from .validators import validate_file_extension


class Game(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)

class User(AbstractUser):
    birth_date = models.DateField(blank=False)    
    last_played = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    REQUIRED_FIELDS = ['birth_date', 'password', 'email']

User = get_user_model()


class PlaySession(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['game', 'created_by']


class Avatar(models.Model):
    file = models.FileField(blank=False, null=False, validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = ['user', 'file']

    def __str__(self):
        return '{} ({})'.format(self.user, self.file)