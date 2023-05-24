from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movies/', views.movie_list),
    path('genres/', views.genre_list),
    path('random/movies/', views.movie_random_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/search_movies_by_genre/', views.search_movies_by_genre),
    path('movies/movie_search/<str:searchKeyword>/', views.movie_search),
    path('movies/favorite/<int:movie_pk>/', views.like),
    path('movies/favorite/list/', views.get_favorite_movies),
]