# from django.db import models
from django.conf import settings
# from movies.models import Movie

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# class Article(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=50)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    

# class Comment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)