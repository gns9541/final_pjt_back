from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': '댓글이 생성되었습니다.'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response({'message': '댓글을 찾을 수 없습니다.'}, status=404)
    
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': '댓글이 수정되었습니다.'}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response({'message': '댓글을 찾을 수 없습니다.'}, status=404)
    
    comment.delete()
    return Response({'message': '댓글이 삭제되었습니다.'}, status=204)