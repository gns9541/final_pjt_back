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
        fields = ('title', 'poster_path', 'vote_average', 'genre_id')

    genre_id = GenreSerializer(many=True)

class MovieDetailSerializers(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    class Meta:
        model = Movie
        fields = ('title', 'poster_path', 'vote_average', 'genre_id', 'overview',)

    genre_id = GenreSerializer(many=True)