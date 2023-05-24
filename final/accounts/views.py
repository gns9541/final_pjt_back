
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    profile_data = {
        'username': user.username,
        'id': user.id,
        # 'email': user.email,
        # 'profile_picture': user.profile_picture.url if user.profile_picture else None,
    }
    return Response(profile_data)


# @api_view(['GET'])
# def profile(request):
#     user = request.user
#     UserModel = get_user_model()
#     try:
#         user_obj = UserModel.objects.get(username=user.username)
#         profile_data = {
#             'username': user_obj.username,
#             'token': user_obj.token
#             # 'email': user_obj.email,
#             # 'profile_picture': user_obj.profile_picture.url if user_obj.profile_picture else None,
#             # 추가 필드가 있다면 해당 필드도 포함시킴
#         }
#         return Response(profile_data)
#     except UserModel.DoesNotExist:
#         return Response({'error': 'User does not exist'}, status=400)



# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     user = request.user
#     UserModel = get_user_model()
#     try:
#         user_obj = UserModel.objects.get(username=user.username)
#         profile_data = {
#             'username': user_obj.username,
#             'token': user_obj.token
#             # 'email': user_obj.email,
#             # 'profile_picture': user_obj.profile_picture.url if user_obj.profile_picture else None,
#             # 추가 필드가 있다면 해당 필드도 포함시킴
#         }
#         return Response(profile_data)
#     except UserModel.DoesNotExist:
#         return Response({'error': 'User does not exist'}, status=400)
