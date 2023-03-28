# users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CreateUser

urlpatterns = [
    path('signup/', CreateUser.as_view(), name='signup'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
]
