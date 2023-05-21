from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Genre
from .serializers import GenreSearchSerializer, MovieSerializer, MovieDetailSerializers, GenreSerializer
import random

from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def movie_list(request):
    if request.method == "GET":
        movies = get_list_or_404(Movie)[:100]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET']) 
def movie_random_list(request):
    movies = list(Movie.objects.filter(released_date__year__gte=1990))
    random.shuffle(movies)
    sliced_movies = movies[:100]  # 100개만 가져오도록 설정
    serializer = MovieSerializer(sliced_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "GET":
        serializer = MovieDetailSerializers(movie)
        return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    if request.method == "GET":
        genres = get_list_or_404(Genre)[:30]
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def search_movies_by_genre(request):
    genre_id = request.GET.get('genre_id')  # Vue에서 선택한 장르 ID
    genre_name = request.GET.get('genre_name')  # Vue에서 선택한 장르 이름

    if genre_id:
        movies = Movie.objects.filter(genre_id=genre_id)
    elif genre_name:
        genre = Genre.objects.filter(name=genre_name).first()
        if genre:
            movies = genre.genre_movies.all()
        else:
            movies = []

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_search(request):
    keyword = request.GET.get('keyword', '')  # 사용자가 입력한 키워드를 가져옴
    
    movies = Movie.objects.filter(Q(title__icontains=keyword)) #| Q(overview__icontains=keyword))
    
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



# @api_view(['GET'])
# def movie_list(request):
#     if request.method == "GET":
#         paginator = PageNumberPagination()
#         paginator.page_size = 5  # 페이지당 10개의 결과를 보여줄 수 있도록 설정
#         movies = get_list_or_404(Movie)

#         result_page = paginator.paginate_queryset(movies, request)
#         serializer = MovieSerializer(result_page, many=True)

#         return paginator.get_paginated_response(serializer.data)
# class MoviePagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100