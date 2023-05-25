from django.db import models
from django.contrib.auth import get_user_model
import requests
import json
import os
from django.conf import settings
from comments.models import Comment



class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateField(blank=True)
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField()
    genre_id = models.ManyToManyField(Genre, related_name='genre_movies', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    comment = models.ManyToManyField(Comment, related_name='comment_movies', blank=True)

    def __str__(self):
        return self.title
    
# User = get_user_model()

# class UserFavoriteMovie(models.Model):
#     user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorited_by')

#     def __str__(self):
#         return f'{self.user.username} - {self.movie.title}'



TMDB_API_KEY = 'f9cf6f37cea2e3d2dc53a3920a71e365'

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', '') and movie.get('poster_path', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genre_id': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures/movies')
    file_path = os.path.join(fixtures_dir, 'movie_data.json')

    with open(file_path, "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

# get_movie_datas()