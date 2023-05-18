from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('', views.create_comment, name='create_comment'),
    path('<int:comment_id>/', views.update_comment, name='update'),
    path('<int:comment_id>/', views.delete_comment, name='delete'),
]