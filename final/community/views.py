from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Article, Comment
from .serializers import ArticleSaveSerializer, ArticleSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def article_create(request):
    print(request.user)
    if request.method == 'POST':
        serializer = ArticleSaveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    
    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def article_update():
        if request.user == article.user:
            serializer = ArticleSaveSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    def article_delete():
        if request.user == article.user:
            article.delete()
            data = {'삭제 완료': '삭제가 완료되었습니다.'}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        return Response({'삭제 안 됨': '작성자가 로그인 사용자가 아님'})
    
    if request.method == 'GET':
        return article_detail()
    
    elif request.method == 'DELETE':
        return article_delete()
    
    elif request.method == 'PUT':
        return article_update()

     
@api_view(['POST'])
def comment_create(request, article_id):
    user = request.user
    article = get_object_or_404(Article, pk=article_id)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=user)

        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, article_id, comment_id):
    article = get_object_or_404(Article, pk=article_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()