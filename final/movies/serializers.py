from rest_framework import serializers
from .models import Movie,Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)


    class Meta:
        model = Movie
        fields = ('movie_id','title', 'poster_path', 'vote_average', 'genre_id','movie_id')

    genre_id = GenreSerializer(many=True)

class MovieDetailSerializers(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    class Meta:
        model = Movie
        fields = ('movie_id','title', 'poster_path', 'vote_average', 'genre_id', 'overview', 'released_date','like_users')

    genre_id = GenreSerializer(many=True)


class GenreSearchSerializer(serializers.Serializer):
    genre_id = serializers.IntegerField(required=False)
    genre_name = serializers.CharField(required=False)

    def validate(self, attrs):
        genre_id = attrs.get('genre_id')
        genre_name = attrs.get('genre_name')

        if not genre_id and not genre_name:
            raise serializers.ValidationError("Either genre_id or genre_name is required.")

        return attrs
    
class GenreMovieSerializers(serializers.ModelSerializer):
    genre_id = GenreSearchSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('title', 'poster_path', 'vote_average', 'genre_id', 'movie_id','like_users')


# class UserFavoriteMovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserFavoriteMovie
#         fields = '__all__'