from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.article_create),
    path('<int:movie_pk>/', views.article_detail_update_delete),
    path('<int:article_id>/comments/', views.comment_create),
    path('<int:article_id>/comments/<int:comment_id>/', views.comment_update_delete),
]