from django.urls import path
from .views import profile

app_name = 'accounts'
urlpatterns = [
    # 다른 URL 패턴들...
    path('api/profile/', profile, name='profile'),
]
