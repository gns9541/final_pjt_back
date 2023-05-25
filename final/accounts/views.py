
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
        'email': user.email if user.email else None
        # 'profile_picture': user.profile_picture.url if user.profile_picture else None,
    }
    return Response(profile_data)


