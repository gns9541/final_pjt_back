from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# from .models import Movie

# Create your models here.
class User(AbstractUser):
    pass


# User = get_user_model()

# class UserFavoriteMovie(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_movies')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorited_by')

#     def __str__(self):
#         return f'{self.user.username} - {self.movie.title}'
