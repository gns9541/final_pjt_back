# from rest_framework import serializers
# from community.models import Article, Comment
# from movies.models import Movie
# from accounts.models import User
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at']

# class CommentSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#                 model = User
#                 fields = ('pk', 'username',)

#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = ('pk', 'user', 'content', 'article', 'created_at', 'updated_at')
#         read_only_fields = ('article', 'created_at', 'updated_at',)


# class ArticleSaveSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#                 model = User
#                 fields = ('pk', 'username',)

#     comments = CommentSerializer(many=True, read_only=True)
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Article
#         fields = ('pk', 'user', 'movie', 'title', 'content',
#                 'comments', 'created_at', 'updated_at')
#         read_only_fields = ('created_at', 'updated_at')




# class ArticleSerializer(serializers.ModelSerializer):
#     class MoviesSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Movie
#             fields = ('pk', 'title', 'poster_path')

#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#                 model = User
#                 fields = ('pk', 'username',)

#     comments = CommentSerializer(many=True, read_only=True)
#     movie = MoviesSerializer(read_only=True)
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Article
#         fields = ('pk', 'user', 'movie', 'title', 'content',
#                 'comments', 'created_at', 'updated_at')
#         read_only_fields = ('created_at', 'updated_at')

