from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Genre
from comments.models import Comment
from accounts.models import User
import json

from .serializers import GenreSearchSerializer, MovieSerializer, MovieDetailSerializers, GenreSerializer
import random

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication

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
def movie_search(request,searchKeyword):
    # searchKeyword = request.GET.get('searchKeyword', '')  # 사용자가 입력한 키워드를 가져옴
    
    movies = Movie.objects.filter(Q(title__icontains=searchKeyword)) #| Q(overview__icontains=searchKeyword))
    
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    
    
@api_view(['GET','POST'])
def like(request, movie_pk):
    if request.method == "POST":
        if request.user.is_authenticated:
            movie = get_object_or_404(Movie, pk=movie_pk)
            # user = request.user

            if movie.like_users.filter(pk=request.user.pk).exists():
                movie.like_users.remove(request.user)
                is_liked = False
            else:
                movie.like_users.add(request.user)
                is_liked = True
            context = {
                'like_count': movie.like_users.count(),
                'is_liked': is_liked,
            }
            return JsonResponse(context)
        return JsonResponse({'message': '잘못된 요청입니다.'}, status=400)
    elif request.method == "GET":
        if request.user.is_authenticated:
            movie = get_object_or_404(Movie, pk=movie_pk)
            if movie.like_users.filter(pk=request.user.pk).exists():
                is_liked = True
            else:
                is_liked = False
            context = {
                'like_count': movie.like_users.count(),
                'is_liked': is_liked,
            }
            return JsonResponse(context)
        return JsonResponse({'message': '잘못된 요청입니다.'}, status=400)



@api_view(['GET'])
def get_favorite_movies(request):
    # user = request.user
    if request.user.is_authenticated:
        liked_movies = Movie.objects.filter(like_users=request.user)
        serialized_movies = [{'title': movie.title, 'movie_id': movie.movie_id, 'poster_path':movie.poster_path, 'vote_average':movie.vote_average} for movie in liked_movies]
        return JsonResponse(serialized_movies, safe=False)
    return JsonResponse({'message': 'Authentication required.'}, status=401)


def add_comment(request, movie_pk):
    if request.method == 'POST':
        # Vue.js로부터 전송된 JSON 데이터를 파싱하여 필요한 정보를 추출
        data = json.loads(request.body)
        text = data['text']
        # user = data['user_id']

        
        movie = get_object_or_404(Movie, movie_pk=movie_pk)

        
        user = request.user

        # Comment 모델에 코멘트 생성
        comment = Comment.objects.create(text=text, user=user)

        # 영화와 코멘트의 ManyToMany 관계 설정
        movie.comment.add(comment)

        # 응답 데이터 전송 (성공 여부 등)
        response_data = {
            'success': True,
            'message': '코멘트가 추가되었습니다.'
        }
        return JsonResponse(response_data)

    # POST 요청이 아닌 다른 요청에 대해서는 404 에러 반환
    return JsonResponse({'error': '잘못된 요청입니다.'}, status=404)


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