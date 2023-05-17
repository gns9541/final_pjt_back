from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.DateTimeField(blank=True)
    vote_average = models.FloatField()
    genre_id = models.ManyToManyField(Genre, related_name='genre_movies', blank=True)

    def __str__(self):
        return self.title


